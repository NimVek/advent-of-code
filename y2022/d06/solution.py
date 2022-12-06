import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def generic(stream, length):
        start = 0
        end = 1
        while end < len(stream):
            __log__.debug((start, end))
            found = stream.rfind(stream[end], max(start, end - length + 1), end)
            __log__.debug(
                (stream[max(start, end - length + 1) : end], stream[end], found)
            )
            if found > -1:
                start = found + 1
            end += 1
            if end - start == length:
                return end
        return -1

    part_01 = functools.partial(generic, length=4)
    part_02 = functools.partial(generic, length=14)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
