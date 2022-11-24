import functools

from aoc.lib.algebra import Direction2D, Vector
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class StandardLayout:
    def __init__(self):
        self.position = Vector(0, 0)

    def move(self, direction):
        newposition = self.position + direction
        __log__.debug(
            (
                self.position,
                direction,
                newposition,
                max(map(abs, newposition)),
                max(map(abs, newposition)) <= 1,
            )
        )
        if max(map(abs, newposition)) <= 1:
            self.position = newposition

    @property
    def button(self):
        __log__.debug(self.position)
        return str(5 + self.position.dot(Vector(-3, 1)))


class DiamondLayout:
    LAYOUT = ("  1  ", " 234 ", "56789", " ABC ", "  D  ")

    def __init__(self):
        self.position = Vector(0, -2)

    def move(self, direction):
        newposition = self.position + direction
        __log__.debug(
            (
                self.position,
                direction,
                newposition,
                newposition.norm(1),
                newposition.norm(1) <= 2,
            )
        )
        if newposition.norm(1) <= 2:
            self.position = newposition

    @property
    def button(self):
        __log__.debug(self.position)
        return DiamondLayout.LAYOUT[2 - self.position[0]][2 + self.position[1]]


class Solution(SolutionBase):
    @staticmethod
    def prepare(instructions):
        return tuple(
            tuple(Direction2D[direction] for direction in line) for line in instructions
        )

    @staticmethod
    def generic(instructions, layout):
        result = ""
        for line in instructions:
            for direction in line:
                layout.move(direction)
            result += layout.button
        return result

    part_01 = functools.partial(generic, layout=StandardLayout())
    part_02 = functools.partial(generic, layout=DiamondLayout())


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
