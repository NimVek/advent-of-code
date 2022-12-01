import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(elves):
        result = []
        for elf in elves:
            if isinstance(elf, str):
                result.append((int(elf),))
            else:
                result.append(tuple(map(int, elf)))
        return result

    @staticmethod
    def generic(elves, top):
        return sum(sorted(map(sum, elves), reverse=True)[:top])

    part_01 = functools.partial(generic, top=1)
    part_02 = functools.partial(generic, top=3)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
