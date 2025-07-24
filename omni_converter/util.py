import os
import cloudpickle as pickle


def get_python_version() -> str:
    import sys
    vi = sys.version_info
    return f"{vi.major}_{vi.minor}_{vi.micro}"


class ShelvedCache:
    """
    a cache that uses shelve and memory as backend
    """

    def __init__(self, path):
        import filelock
        self.p_version = get_python_version()
        self.path = path + self.p_version
        self.lock = filelock.FileLock(path + self.p_version + ".lock")
        self.mem_cache = dict()

    def get_cache(self):
        import shelve
        return shelve.open(self.path, writeback=True)

    def __contains__(self, key):
        key = pickle.dumps(key, 0).decode()
        if key in self.mem_cache:
            return True
        else:
            with self.lock, self.get_cache() as db:
                return key in db


    def __setitem__(self, key, value):
        from loguru import logger
        logger.debug("waiting lock for saving conversion")
        with self.lock:
            with self.get_cache() as db:
                self._set_inlock(key, value, db)

    def _set_inlock(self, key, value, db):
        from loguru import logger
        logger.debug("writing..")
        key = str(pickle.dumps(key, 0))
        self.mem_cache[key] = value
        db[key] = value
        db.sync()

    def __getitem__(self, key):
        try:
            import cloudpickle as pickle
            db_key = str(pickle.dumps(key, 0))
        except Exception as e:
            raise RuntimeError(f"cannot pickle key:{key} due to {e}")
        if db_key in self.mem_cache:
            return self.mem_cache[db_key]
        with self.lock:
            failed = True
            with self.get_cache() as db:
                if db_key in db:
                    try:
                        res = db[db_key]
                        self.mem_cache[db_key] = res
                        failed = False
                    except Exception:
                        from loguru import logger
                        logger.warning(f"failed to load from shelve.key={key}")
            if failed:
                return self.__missing__(key)
            return res

    def __missing__(self, key):
        raise KeyError(key)

    def items(self):
        with self.lock, self.get_cache() as db:
            for k, v in db.items():
                yield pickle.loads(k.encode()), v

    def clear(self):
        with self.lock:
            os.remove(self.path + ".db")


class DefaultShelveCache(ShelvedCache):
    def __init__(self, f, path):
        super().__init__(path)
        self.f = f

    def __missing__(self, origkey):
        from loguru import logger
        logger.warning(f"cannot find conversion:{origkey}")
        res = self.f(origkey)
        logger.warning(f"found res for {origkey}")
        try:
            logger.debug(f"saving conversion for {origkey}")
            with self.get_cache() as db:
                self._set_inlock(origkey, res, db)
            # self[origkey] = res
            logger.debug(f"saved conversion for {origkey}")
        except Exception:
            logger.error(f"cannot save data \n\t{res} to key \n\t{origkey} of shelve.")
        return res
