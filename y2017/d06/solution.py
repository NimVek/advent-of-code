import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(map(int, data.split()))

    @staticmethod
    def generic(banks, final):
        length = len(banks)
        reached = []
        while banks not in reached:
            reached.append(banks)
            __log__.debug(banks)
            m = max(banks)
            idx = banks.index(m)
            banks = list(banks)
            banks[idx] = 0
            banks = [x + m // length for x in banks]
            for i in range(m % length):
                banks[(idx + 1 + i) % length] += 1
            banks = tuple(banks)
        return final(reached, banks)

    part_01 = functools.partial(generic, final=lambda reached, banks: len(reached))
    part_02 = functools.partial(
        generic, final=lambda reached, banks: len(reached) - reached.index(banks)
    )


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
