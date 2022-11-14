import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return [line.split() for line in data]

    @staticmethod
    def valid_01(passphrase):
        return len(passphrase) == len(set(passphrase))

    @staticmethod
    def valid_02(passphrase):
        return Solution.valid_01(["".join(sorted(word)) for word in passphrase])

    @staticmethod
    def generic(data, valid):
        return sum(valid(passphrase) for passphrase in data)

    part_01 = functools.partial(generic, valid=valid_01)
    part_02 = functools.partial(generic, valid=valid_02)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
