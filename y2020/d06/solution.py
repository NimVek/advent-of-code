import functools
import operator

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        if not any(isinstance(entry, list) for entry in data):
            data = [data]
        result = []
        for entry in data:
            if isinstance(entry, str):
                result.append([set(entry)])
            else:
                result.append([set(e) for e in entry])
        return tuple(result)

    @staticmethod
    def generic(data, function):
        return sum(len(functools.reduce(function, entry)) for entry in data)

    part_01 = functools.partial(generic, function=operator.__or__)
    part_02 = functools.partial(generic, function=operator.__and__)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
