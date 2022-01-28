import os
import pickle

from loguru import logger


class ShelvedCache:
    """
    a cache that uses shelve and memory as backend
    """

    def __init__(self, path):
        import filelock
        self.path = path
        self.lock = filelock.FileLock(path + ".lock")
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
        with self.lock, self.get_cache() as db:
            key = pickle.dumps(key, 0).decode()
            self.mem_cache[key] = value
            db[key] = value
            db.sync()

    def __getitem__(self, key):
        with self.lock:
            key = pickle.dumps(key, 0).decode()
            if key in self.mem_cache:
                return self.mem_cache[key]
            else:
                with self.get_cache() as db:
                    if key in db:
                        try:
                            res = db[key]
                            self.mem_cache[key] = res
                        except Exception as e:
                            logger.warning(f"failed to load from shelve.key={key}")
                            return self.__missing__(key)
                        return res
                    else:
                        return self.__missing__(key)

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

    @logger.catch
    def __missing__(self, key):
        with self.lock:
            jsonkey = pickle.loads(key.encode())
            res = self.f(jsonkey)
            try:
                self[jsonkey] = res
            except Exception as e:
                logger.error(f"cannot save data \n\t{res} to key \n\t{key} of shelve.")
            return res