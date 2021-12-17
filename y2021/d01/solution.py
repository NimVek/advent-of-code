import functools
import logging

from aoc.lib.solution import SolutionBase


__all__ = ["Solution"]
logger = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return list(map(int, data))

    @staticmethod
    def generic(data, window_size):
        return sum(map(lambda deep: deep[0] < deep[1], zip(data, data[window_size:])))

    part_01 = functools.partialmethod(generic, window_size=1)
    part_02 = functools.partialmethod(generic, window_size=3)
