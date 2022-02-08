import os
import pickle

from loguru import logger


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
        with self.lock, self.get_cache() as db:
            key = pickle.dumps(key, 0).decode()
            if key in self.mem_cache:
                return True
            else:
                return key in db

    def __setitem__(self, key, value):
        logger.debug(f"waiting lock for saving conversion")
        with self.lock:
            with self.get_cache() as db:
                self._set_inlock(key, value, db)

    def _set_inlock(self, key, value, db):
        logger.debug(f"writing..")
        key = pickle.dumps(key, 0).decode()
        self.mem_cache[key] = value
        db[key] = value
        db.sync()

    def __getitem__(self, key):
        with self.lock:
            try:
                key = pickle.dumps(key, 0).decode()
            except Exception as e:
                raise RuntimeError(f"cannot pickle key:{key}")
            if key in self.mem_cache:
                return self.mem_cache[key]
            else:
                failed = True
                with self.get_cache() as db:
                    if key in db:
                        try:
                            res = db[key]
                            self.mem_cache[key] = res
                            failed = False
                        except Exception as e:
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

    def __missing__(self, key):
        origkey = pickle.loads(key.encode())
        logger.warning(f"cannot find conversion:{origkey}")
        res = self.f(origkey)
        logger.warning(f"found res for {origkey}")
        try:
            logger.debug(f"saving conversion for {origkey}")
            with self.get_cache() as db:
                self._set_inlock(origkey, res, db)
            # self[origkey] = res
            logger.debug(f"saved conversion for {origkey}")
        except Exception as e:
            logger.error(f"cannot save data \n\t{res} to key \n\t{key} of shelve.")
        return res
