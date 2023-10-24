from aoc.lib.solution import SolutionBase

import logging
from collections import Counter, defaultdict
import functools

__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return Counter(map(int, data.split(",")))

    @staticmethod
    def generic(population, days):
        for _ in range(days):
            fishes = defaultdict(int)
            for timer, fish in population.items():
                if timer == 0:
                    fishes[8] = fish
                    fishes[6] += fish
                else:
                    fishes[timer - 1] += fish
            population = fishes
        return sum(population.values())

    part_01 = functools.partial(generic, days=80)
    part_02 = functools.partial(generic, days=256)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
