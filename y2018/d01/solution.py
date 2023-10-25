import itertools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(map(int, data))

    @staticmethod
    def part_01(data):
        return sum(data)

    @staticmethod
    def part_02(data):
        seen = set()
        frequency = 0
        for change in itertools.cycle(data):
            seen.add(frequency)
            frequency += change
            if frequency in seen:
                break
        return frequency


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
