import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(map(int, data))

    @staticmethod
    def fuel(mass):
        return (mass // 3) - 2

    @staticmethod
    def fuelfuel(mass):
        result = 0
        while mass > 0:
            mass = max(Solution.fuel(mass), 0)
            result += mass
        return result

    @staticmethod
    def generic(data, func):
        return sum(map(func, data))

    part_01 = functools.partial(generic, func=fuel)
    part_02 = functools.partial(generic, func=fuelfuel)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
