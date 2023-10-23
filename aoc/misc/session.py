import hashlib
import pathlib

import furl
import requests

import logging


__log__ = logging.getLogger(__name__)


class Session(requests.Session):
    def __init__(self, base):
        super().__init__()
        self.base = base

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = furl.furl(base)
        self.__base.path.normalize()
        self.__base.remove(path="/")

    def request(self, method, url, *args, **kwargs):
        return super().request(method, self.base / url, *args, **kwargs)


class CachedSession(Session):
    def __init__(self, cache_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache_dir = pathlib.Path(cache_dir)

    def cache_file(self, url):
        return self.__cache_dir / hashlib.sha256(url.encode()).hexdigest()

    def request(self, method, url, *args, **kwargs):
        if method == "GET":
            cache_file = self.cache_file(url)
            if cache_file.exists():
                with cache_file.open("r") as f:
                    return f.read()

        result = super().request(method, url, *args, **kwargs)
        result.raise_for_status()
        result = result.text

        cache_file = self.cache_file(url)
        if method != "GET":
            import time

            cache_file = cache_file.with_suffix(f".{method}.{int(time.time())}")
        with cache_file.open("w") as f:
            f.write(result)

        return result

    def purge(self, url):
        __log__.info("Purge URL %s", url)
        cache_file = self.cache_file(url)
        cache_file.unlink(missing_ok=True)
