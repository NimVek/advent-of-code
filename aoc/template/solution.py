import logging

from aoc.lib.solution import SolutionBase


__all__ = ["Solution"]
logger = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def part_01(data):
        raise NotImplementedError

    @staticmethod
    def part_02(data):
        raise NotImplementedError
