from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    table = str.maketrans("BFRL", "1010")

    @staticmethod
    def seat_id(line):
        return int(line.translate(Solution.table), 2)

    @staticmethod
    def part_01(data):
        return max(Solution.seat_id(seat) for seat in data)

    @staticmethod
    def part_02(data):
        ids = [Solution.seat_id(seat) for seat in data]
        low, high = min(ids), max(ids)
        return ((high * (high + 1)) - (low * (low - 1))) // 2 - sum(ids)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
