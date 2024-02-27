import functools
import itertools

from aoc.lib.grid import Direction2D, Origin2D
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)

DIRECTIONS = {
    "^": Direction2D.NORTH,
    "v": Direction2D.SOUTH,
    ">": Direction2D.EAST,
    "<": Direction2D.WEST,
}


class Santa:
    def __init__(self):
        self.location = Origin2D
        self.houses = {self.location}

    def move(self, direction):
        self.location += direction
        self.houses.add(self.location)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(DIRECTIONS[direction] for direction in data)

    @staticmethod
    def generic(directions, santas):
        santas = [Santa() for _ in range(santas)]
        for santa, direction in zip(itertools.cycle(santas), directions):
            santa.move(direction)
        return len(set.union(*(santa.houses for santa in santas)))

    part_01 = functools.partial(generic, santas=1)
    part_02 = functools.partial(generic, santas=2)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
