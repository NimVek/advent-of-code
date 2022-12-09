import functools

from aoc.lib.grid import Direction2D, Origin2D
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Rope(list):
    def __init__(self, length):
        super().__init__([Origin2D] * length)

    def move(self, direction):
        self[0] += direction
        for i in range(len(self) - 1):
            difference = self[i] - self[i + 1]
            max_difference = max(map(abs, difference))
            if max_difference > 1:
                max_difference -= 1
                difference = (
                    min(max(j, -max_difference), max_difference) for j in difference
                )
                self[i + 1] += difference

    @property
    def tail(self):
        return self[-1]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            (Direction2D[direction], int(c))
            for direction, c in (x.split() for x in data)
        )

    @staticmethod
    def generic(directions, length):
        rope = Rope(length=length)
        positions = {rope.tail}
        for direction, c in directions:
            for _ in range(c):
                rope.move(direction)
                positions.add(rope.tail)
        return len(positions)

    part_01 = functools.partial(generic, length=2)
    part_02 = functools.partial(generic, length=10)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
