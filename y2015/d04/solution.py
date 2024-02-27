import functools
import hashlib
import itertools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def generic(key, zeroes):
        for number in itertools.count():
            if (
                hashlib.md5(f"{key}{number}".encode())
                .hexdigest()
                .startswith("0" * zeroes)
            ):
                return number

    part_01 = functools.partial(generic, zeroes=5)
    part_01.marker = ["slow"]
    part_02 = functools.partial(generic, zeroes=6)
    part_02.marker = ["slow"]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
