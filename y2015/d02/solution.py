from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Present(list):
    def __init__(self, *sides):
        super().__init__(sorted(sides))

    @property
    def paper(self):
        return 3 * self[0] * self[1] + 2 * self[1] * self[2] + 2 * self[2] * self[0]

    @property
    def ribbon(self):
        return 2 * self[0] + 2 * self[1] + self[0] * self[1] * self[2]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        if isinstance(data, str):
            data = [data]
        return [Present(*(map(int, row.split("x")))) for row in data]

    @staticmethod
    def part_01(data):
        return sum(present.paper for present in data)

    @staticmethod
    def part_02(data):
        return sum(present.ribbon for present in data)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
