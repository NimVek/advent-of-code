import functools

from dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Interval:
    lower: int
    upper: int


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        result = []
        for line in data:
            result.append(
                [
                    Interval(*map(int, assignment.split("-")))
                    for assignment in line.split(",")
                ]
            )
        return result

    @staticmethod
    def generic(assignments, evaluation):
        return sum(evaluation(*intervals) for intervals in assignments)

    @staticmethod
    def contains(first, second):
        return (
            first.lower <= second.lower
            and first.upper >= second.upper
            or first.lower >= second.lower
            and first.upper <= second.upper
        )

    @staticmethod
    def overlaps(first, second):
        return first.upper >= second.lower and first.lower <= second.upper

    part_01 = functools.partial(generic, evaluation=contains)
    part_02 = functools.partial(generic, evaluation=overlaps)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
