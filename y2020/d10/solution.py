import collections

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return sorted(map(int, data))

    @staticmethod
    def part_01(data):
        differences = collections.Counter(
            high - low for low, high in zip([0] + data, data + [data[-1] + 3])
        )
        return differences[1] * differences[3]

    @staticmethod
    def part_02(data):
        arrangements = collections.defaultdict(int, {0: 1})
        for joltage in data:
            arrangements[joltage] = (
                arrangements[joltage - 3]
                + arrangements[joltage - 2]
                + arrangements[joltage - 1]
            )
        return arrangements[data[-1]]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
