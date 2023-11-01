import functools

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Instruction:
    direction: str
    units: int


class SimpleSubmarine:
    def __init__(self):
        self.horizontal = 0
        self.__depth = 0

    @property
    def depth(self):
        return self.__depth

    def forward(self, i):
        self.horizontal += i

    def up(self, i):
        self.__depth -= i

    def down(self, i):
        self.__depth += i

    def distance(self):
        return self.horizontal * self.depth


class ComplexSubmarine(SimpleSubmarine):
    def __init__(self):
        super().__init__()
        self.__depth = 0

    @property
    def aim(self):
        return super().depth

    @property
    def depth(self):
        return self.__depth

    def forward(self, i):
        super().forward(i)
        self.__depth += self.aim * i


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            Instruction(direction, int(units))
            for direction, units in (line.split() for line in data)
        )

    @staticmethod
    def generic(data, submarine_cls):
        submarine = submarine_cls()
        for instruction in data:
            getattr(submarine, instruction.direction)(instruction.units)
        return submarine.distance()

    part_01 = functools.partial(generic, submarine=SimpleSubmarine)
    part_02 = functools.partial(generic, submarine=ComplexSubmarine)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
