from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def priority(item):
        if "a" <= item <= "z":
            return ord(item) - ord("a") + 1
        return ord(item) - ord("A") + 27

    @staticmethod
    def generic(groups):
        result = 0
        for group in groups:
            first, *other = map(set, group)
            first.intersection_update(*other)
            __log__.debug(first)
            result += sum(Solution.priority(item) for item in first)
        return result

    @staticmethod
    def part_01(elves):
        return Solution.generic(
            (rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :])
            for rucksack in elves
        )

    @staticmethod
    def part_02(elves):
        return Solution.generic(zip(*(iter(elves),) * 3))


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
