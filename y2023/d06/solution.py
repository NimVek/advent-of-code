import math

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Data:
    time: tuple[int, ...]
    distance: tuple[int, ...]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return Data(
            time=tuple(map(int, data[0][5:].split())),
            distance=tuple(map(int, data[1][9:].split())),
        )

    @staticmethod
    def ways(time, distance):
        sqrt = math.sqrt(time**2 - 4 * distance)
        return math.ceil(0.5 * (time + sqrt)) - math.floor(0.5 * (time - sqrt)) - 1

    @staticmethod
    def part_01(data):
        return math.prod(
            Solution.ways(time, distance)
            for time, distance in zip(data.time, data.distance)
        )

    @staticmethod
    def part_02(data):
        time = int("".join(map(str, data.time)))
        distance = int("".join(map(str, data.distance)))
        return Solution.ways(time, distance)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
