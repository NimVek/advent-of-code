import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def digit(line):
        if str.isdigit(line[0]):
            return int(line[0])
        return None

    @staticmethod
    def advanced_digit(line):
        if result := Solution.digit(line):
            return result

        for idx, digit in enumerate(Solution.DIGITS, start=1):
            if line.startswith(digit):
                return idx
        return None

    @staticmethod
    def generic(data, function):
        result = 0

        for line in data:
            for idx in range(len(line)):
                if digit := function(line[idx:]):
                    result += 10 * digit
                    break
            for idx in range(len(line) - 1, -1, -1):
                if digit := function(line[idx:]):
                    result += digit
                    break
        return result

    part_01 = functools.partial(generic, function=digit)
    part_02 = functools.partial(generic, function=advanced_digit)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
