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
        return sum(len(line) - len(eval(line)) for line in data)

    @staticmethod
    def part_02(data):
        return sum(2 + line.count("\\") + line.count('"') for line in data)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
