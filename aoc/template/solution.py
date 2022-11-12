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
        raise NotImplementedError

    @staticmethod
    def part_02(data):
        raise NotImplementedError


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
