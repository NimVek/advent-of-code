import collections

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)

import json


@dataclass
class OpCode:
    A: int
    B: int
    C: int

    def __call__(self, register: tuple[int, ...]) -> tuple[int, ...]:
        result = list(register)
        result[self.C] = self.result(register)
        return tuple(result)

    def __str__(self):
        return f"{self.__class__.__name__.lower()} {self.A} {self.B} {self.C}"


class RegisterRegister(OpCode):
    def result(self, register) -> int:
        return self.operation(register[self.A], register[self.B])


class RegisterImmediate(OpCode):
    def result(self, register) -> int:
        return self.operation(register[self.A], self.B)


class ImmediateRegister(OpCode):
    def result(self, register) -> int:
        return self.operation(self.A, register[self.B])


class Addition(OpCode):
    def operation(self, A, B):
        return A + B


class Multiplication(OpCode):
    def operation(self, A, B):
        return A * B


class BitwiseAnd(OpCode):
    def operation(self, A, B):
        return A & B


class BitwiseOr(OpCode):
    def operation(self, A, B):
        return A | B


class Assignment(OpCode):
    def operation(self, A, _):
        return A


class GreaterThan(OpCode):
    def operation(self, A, B):
        return 1 if A > B else 0


class Equal(OpCode):
    def operation(self, A, B):
        return 1 if A == B else 0


class AddR(Addition, RegisterRegister):
    pass


class AddI(Addition, RegisterImmediate):
    pass


class MulR(Multiplication, RegisterRegister):
    pass


class MulI(Multiplication, RegisterImmediate):
    pass


class BAnR(BitwiseAnd, RegisterRegister):
    pass


class BAnI(BitwiseAnd, RegisterImmediate):
    pass


class BOrR(BitwiseOr, RegisterRegister):
    pass


class BOrI(BitwiseOr, RegisterImmediate):
    pass


class SetR(Assignment, RegisterRegister):
    pass


class SetI(Assignment, ImmediateRegister):
    pass


class GtIR(GreaterThan, ImmediateRegister):
    pass


class GtRI(GreaterThan, RegisterImmediate):
    pass


class GtRR(GreaterThan, RegisterRegister):
    pass


class EqIR(Equal, ImmediateRegister):
    pass


class EqRI(Equal, RegisterImmediate):
    pass


class EqRR(Equal, RegisterRegister):
    pass


def leafclasses(cls):
    return (
        set().union(s for c in cls.__subclasses__() for s in leafclasses(c))
        if cls.__subclasses__()
        else {cls}
    )


opcodes = leafclasses(OpCode)

d = EqRR(*(1, 2, 3))


@dataclass
class Sample:
    before: tuple[int, int, int, int]
    instruction: tuple[int, int, int, int]
    after: tuple[int, int, int, int]


@dataclass
class Input:
    samples: tuple[Sample, ...]
    program: tuple[tuple[int, int, int, int], ...]


@dataclass
class SampleTest:
    code: int
    opportunities: set[type[OpCode]]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        *samples, program = data
        samples = tuple(
            Sample(
                before=tuple(json.loads(s[0][8:])),
                instruction=tuple(map(int, s[1].split())),
                after=tuple(json.loads(s[2][8:])),
            )
            for s in samples
        )
        return Input(
            samples=samples,
            program=tuple(
                tuple(map(int, instruction.split())) for instruction in program
            ),
        )

    @staticmethod
    def test_samples(samples):
        return (
            SampleTest(
                code=sample.instruction[0],
                opportunities={
                    opcode
                    for opcode in opcodes
                    if opcode(*(sample.instruction[1:]))(sample.before) == sample.after
                },
            )
            for sample in samples
        )

    @staticmethod
    def part_01(data):
        return sum(
            1
            for sample in Solution.test_samples(data.samples)
            if len(sample.opportunities) >= 3
        )

    @staticmethod
    def part_02(data):
        investigate = collections.defaultdict(lambda: set(opcodes))
        for sample in Solution.test_samples(data.samples):
            investigate[sample.code] &= sample.opportunities
        translate = dict()
        while investigate:
            translate.update(
                {
                    code: opcodes.pop()
                    for code, opcodes in investigate.items()
                    if len(opcodes) == 1
                }
            )
            investigate = {
                code: opcodes - set(translate.values())
                for code, opcodes in investigate.items()
                if len(opcodes) > 1
            }

        program = tuple(
            translate[instruction[0]](*(instruction[1:]))
            for instruction in data.program
        )

        register = (0, 0, 0, 0)
        for instruction in program:
            register = instruction(register)
        return register[0]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
