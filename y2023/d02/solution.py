import math
import operator

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Sample:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class Game:
    id: int
    samples: tuple[Sample, ...]

    @property
    def power(self):
        return math.prod(
            max(map(operator.attrgetter(color), self.samples))
            for color in ["red", "green", "blue"]
        )

    def possible(self, red, green, blue):
        for sample in self.samples:
            if red < sample.red or green < sample.green or blue < sample.blue:
                return False
        return True


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            Game(
                id=int(game[5:]),
                samples=tuple(
                    Sample(
                        **{
                            color: int(_count)
                            for _count, color in (
                                cube.split() for cube in sample.split(",")
                            )
                        }
                    )
                    for sample in samples.split(";")
                ),
            )
            for game, samples in (line.split(":") for line in data)
        )

    @staticmethod
    def part_01(data):
        return sum(game.id for game in data if game.possible(red=12, green=13, blue=14))

    @staticmethod
    def part_02(data):
        return sum(map(operator.attrgetter("power"), data))


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
