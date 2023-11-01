from collections.abc import Sequence

from pydantic.dataclasses import dataclass

import logging


__all__ = ["OpCode", "Device"]
__log__ = logging.getLogger(__name__)


@dataclass
class OpCode:
    A: int
    B: int
    C: int

    def __call__(self, register: Sequence[int]) -> list[int]:
        result = list(register)
        result[self.C] = self.result(register)
        return result

    @property
    def mnemonic(cls):
        return cls.__class__.__name__.lower()

    def __str__(self):
        return f"{self.mnemonic} {self.A} {self.B} {self.C}"


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


@dataclass
class Device:
    program: tuple[OpCode, ...]
    register: list[int] | None = None
    ip: int | None = None

    def __post_init__(self) -> None:
        if self.register is None:
            if self.ip is None:
                self.register = [0, 0, 0, 0]
            else:
                self.register = [0, 0, 0, 0, 0, 0]
        self._instruction_pointer = 0

    @property
    def instruction_pointer(self):
        if self.ip is None:
            return self._instruction_pointer
        return self.register[self.ip]

    @instruction_pointer.setter
    def instruction_pointer(self, value):
        if self.ip is None:
            self._instruction_pointer = value
        else:
            self.register[self.ip] = value

    def step(self):
        opcode = self.program[self.instruction_pointer]
        before = self.register
        self.register = opcode(before)
        __log__.info(
            "ip=%d %r %s %r", self.instruction_pointer, before, opcode, self.register
        )
        self.instruction_pointer += 1

    def run(self):
        while 0 <= self.instruction_pointer < len(self.program):
            self.step()

    opcodes = leafclasses(OpCode)
