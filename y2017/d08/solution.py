import enum

from collections import defaultdict
from dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Modifier(enum.IntEnum):
    inc = 1
    dec = -1


class Comparator(str, enum.Enum):
    eq = ("==", lambda a, b: a == b)
    ne = ("!=", lambda a, b: a != b)
    lt = ("<", lambda a, b: a < b)
    gt = (">", lambda a, b: a > b)
    le = ("<=", lambda a, b: a <= b)
    ge = (">=", lambda a, b: a >= b)

    def __new__(cls, value, function):
        obj = str.__new__(cls, [value])
        obj._value_ = value
        obj.function = function
        return obj

    def __call__(self, a, b):
        return self.function(a, b)


@dataclass
class Instruction:
    register: str
    modifier: Modifier
    value: int
    compare_register: str
    comparator: Comparator
    compare_value: int

    def __call__(self, register):
        if self.comparator(register[self.compare_register], self.compare_value):
            register[self.register] += self.modifier.value * self.value
        return register[self.register]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        instructions = []
        for instruction in data:
            (
                register,
                modifier,
                value,
                _,
                compare_register,
                comparator,
                compare_value,
            ) = instruction.split()
            instruction = Instruction(
                register,
                Modifier[modifier],
                int(value),
                compare_register,
                Comparator(comparator),
                int(compare_value),
            )
            __log__.debug(instruction)
            instructions.append(instruction)
        return instructions

    @staticmethod
    def part_01(instructions):
        register = defaultdict(int)
        for instruction in instructions:
            instruction(register)
        return max(register.values())

    @staticmethod
    def part_02(instructions):
        register = defaultdict(int)
        return max(instruction(register) for instruction in instructions)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
