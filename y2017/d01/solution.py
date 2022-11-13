import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return [int(i) for i in data]

    @staticmethod
    def generic(data, offset):
        return sum(a for a, b in zip(data, data[offset:] + data[:offset]) if a == b)

    part_01 = functools.partial(generic, offset=1)

    @staticmethod
    def part_02(data):
        return Solution.generic(data, len(data) // 2)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
