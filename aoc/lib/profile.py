import cProfile

import logging


__log__ = logging.getLogger(__name__)


def profile(func):
    def wrapper(*args, **kwargs):
        wrapper.__profile__ = cProfile.Profile()
        return wrapper.__profile__.runcall(func, *args, **kwargs)

    return wrapper
