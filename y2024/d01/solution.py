import collections
import operator

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(zip(*(map(int, row.split()) for row in data)))

    @staticmethod
    def part_01(data):
        return sum(map(abs, (operator.sub(*row) for row in zip(*map(sorted, data)))))

    @staticmethod
    def part_02(data):
        lists = tuple(map(collections.Counter, data))
        return sum(key * lists[0][key] * lists[1][key] for key in lists[0])


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
