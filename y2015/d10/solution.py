import functools
import itertools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def look_and_say(sequence):
        return "".join(
            f"{len(list(group))}{key}" for key, group in itertools.groupby(sequence)
        )

    @staticmethod
    def generic(sequence, times):
        for _ in range(times):
            sequence = Solution.look_and_say(sequence)
        return len(sequence)

    part_01 = functools.partial(generic, times=40)
    part_02 = functools.partial(generic, times=50)
    part_02.marker = ["slow"]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
