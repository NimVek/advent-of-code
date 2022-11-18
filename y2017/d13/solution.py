import itertools
import math

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return dict(map(int, line.split(": ")) for line in data)

    @staticmethod
    def part_01(data):
        return sum(
            depth * _range
            for depth, _range in data.items()
            if depth % ((_range - 1) * 2) == 0
        )

    @staticmethod
    def part_02(data):
        period = 1
        safe = [0]
        for depth, _range in data.items():
            steps = (_range - 1) * 2
            lcm = math.lcm(period, steps)
            safe = [sum(i) for i in itertools.product(range(0, lcm, period), safe)]
            safe = [i for i in safe if (i % steps) != (-depth % steps)]
            period = lcm
            __log__.debug((period, safe))
        return safe[0]


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
