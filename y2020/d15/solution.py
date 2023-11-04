import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(int(i) for i in data.split(","))

    @staticmethod
    def generic(data: list[int], idx: int):
        numbers = {}
        for i, previous in enumerate(data, start=1):
            numbers[previous] = i
        for i in range(i, idx):
            numbers[previous], previous = i, i - numbers.get(previous, i)
        return previous

    part_01 = functools.partial(generic, idx=2020)

    part_02 = functools.partial(generic, idx=30000000)
    part_02.marker = ["slow"]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
