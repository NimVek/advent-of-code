import functools

from aoc.lib.sets import Interval
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        result = []
        for line in data:
            result.append(
                [
                    Interval(map(int, assignment.split("-")))
                    for assignment in line.split(",")
                ]
            )
        return result

    @staticmethod
    def generic(assignments, evaluation):
        return sum(evaluation(*intervals) for intervals in assignments)

    @staticmethod
    def contains(first, second):
        return first in second or second in first

    @staticmethod
    def overlaps(first, second):
        return bool(first & second)

    part_01 = functools.partial(generic, evaluation=contains)
    part_02 = functools.partial(generic, evaluation=overlaps)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
