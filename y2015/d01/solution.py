from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def part_01(data):
        return data.count("(") - data.count(")")

    @staticmethod
    def part_02(data):
        floor = 0
        for idx, val in enumerate(data):
            if val == "(":
                floor += 1
            if val == ")":
                floor -= 1
            if floor < 0:
                return idx + 1


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
