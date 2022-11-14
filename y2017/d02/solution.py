import itertools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return [sorted(int(item) for item in line.split()) for line in data]

    @staticmethod
    def part_01(data):
        return sum(_max - _min for _min, *_, _max in data)

    @staticmethod
    def part_02(data):
        return sum(
            big // small
            for line in data
            for small, big in itertools.combinations(line, 2)
            if big % small == 0
        )


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
