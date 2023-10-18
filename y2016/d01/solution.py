import functools

from aoc.lib.grid import Direction2D, Origin2D, Rotation2D
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Navigator:
    def __init__(self):
        self.location = Origin2D
        self.direction = Direction2D.NORTH

    def turn(self, turn):
        self.direction = Direction2D(turn * self.direction)

    def steps(self, blocks):
        for _ in range(blocks):
            self.location += self.direction
            yield self.location

    def walk(self, instructions):
        for turn, blocks in instructions:
            self.turn(turn)
            yield from self.steps(blocks)


class TwiceNavigator(Navigator):
    def walk(self, instructions):
        steps = set()
        for step in super().walk(instructions):
            yield step
            if step in steps:
                break
            steps.add(step)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple((Rotation2D[i[0]], int(i[1:])) for i in data.split(", "))

    @staticmethod
    def generic(instructions, navigator):
        *_, last = navigator().walk(instructions)
        return int(last.norm(1))

    part_01 = functools.partial(generic, navigator=Navigator)
    part_02 = functools.partial(generic, navigator=TwiceNavigator)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
