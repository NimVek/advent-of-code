import functools
import re

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def nice_01(string):
        return bool(
            (len(re.findall(r"[aeiou]", string)) > 2)
            and re.search(r"(.)\1", string)
            and not re.search(r"(ab|cd|pq|xy)", string)
        )

    @staticmethod
    def nice_02(string):
        return bool(re.search(r"(..).*\1", string) and re.search(r"(.).\1", string))

    @staticmethod
    def generic(data, ruler):
        return sum(ruler(line) for line in data)

    part_01 = functools.partial(generic, ruler=nice_01)
    part_02 = functools.partial(generic, ruler=nice_02)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
