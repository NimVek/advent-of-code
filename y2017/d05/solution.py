import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return list(map(int, data))

    @staticmethod
    def generic(data, increase):
        data = list(data)
        idx = 0
        step = 0
        while idx >= 0 and idx < len(data):
            step += 1
            value = data[idx]
            data[idx] += increase(value)
            idx += value
        return step

    part_01 = functools.partial(generic, increase=lambda x: 1)
    part_02 = functools.partial(generic, increase=lambda x: 1 if x < 3 else -1)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
