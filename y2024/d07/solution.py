import functools

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Equation:
    value: int
    numbers: tuple[int, ...]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            Equation(value=int(numbers[0][:-1]), numbers=tuple(map(int, numbers[1:])))
            for numbers in (row.split() for row in data)
        )

    @staticmethod
    def subtract(minuend, subtrahend):
        if subtrahend > minuend:
            raise ArithmeticError
        return minuend - subtrahend

    @staticmethod
    def divide(dividend, divisor):
        quotient, remainder = divmod(dividend, divisor)
        if remainder:
            raise ArithmeticError
        return quotient

    @staticmethod
    def dissociate(number, suffix):
        number, suffix = str(number), str(suffix)
        if not number.endswith(suffix):
            raise ArithmeticError
        return int(number.removesuffix(suffix))

    @staticmethod
    def calculable(operators, value, numbers):
        *numbers, number = numbers
        if not numbers:
            return value == number
        for operator in operators:
            try:
                if Solution.calculable(operators, operator(value, number), numbers):
                    return True
            except ArithmeticError:
                pass
        return False

    @staticmethod
    def generic(equations, operators):
        return sum(
            equation.value
            for equation in equations
            if Solution.calculable(operators, equation.value, equation.numbers)
        )

    part_01 = functools.partial(generic, operators=[subtract, divide])
    part_02 = functools.partial(generic, operators=[subtract, divide, dissociate])


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
