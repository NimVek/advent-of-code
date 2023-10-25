import collections

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def part_01(data):
        occurrence = collections.Counter()
        for box in data:
            occurrence.update(set(collections.Counter(box).values()))
        return occurrence[2] * occurrence[3]

    @staticmethod
    def part_02(data):
        for idx in range(len(data[0])):
            seen = set()
            for box in data:
                common = box[:idx] + box[idx + 1 :]
                if common in seen:
                    return common
                seen.add(common)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
