import itertools
import json

from collections.abc import Sequence

from aoc.lib.solution import SolutionBase
from aoc.lib.tree import BinaryNode

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class SnailfishNumber(BinaryNode):
    @property
    def magnitude(self):
        if isinstance(self.value, Sequence):
            return 3 * self.value[0].magnitude + 2 * self.value[1].magnitude
        else:
            return self.value

    def _explode(self):
        if self.is_leaf:
            return False
        else:
            if self.depth > 3:
                if previous_leaf := self.left.previous_leaf():
                    previous_leaf.value += self.left.value
                if next_leaf := self.right.next_leaf():
                    next_leaf.value += self.right.value
                self.value = 0
                return True
            else:
                return self.left._explode() or self.right._explode()

    def _split(self):
        if self.is_leaf:
            if self.value > 9:
                half = self.value // 2
                self.value = [
                    SnailfishNumber(half, self),
                    SnailfishNumber(self.value - half, self),
                ]
                return True
            else:
                return False
        else:
            return self.left._split() or self.right._split()

    def _reduce(self):
        while self._explode() or self._split():
            pass

    def __add__(self, other):
        result = SnailfishNumber([self, other])
        result._reduce()
        return result


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return [SnailfishNumber(json.loads(line)) for line in data]

    @staticmethod
    def part_01(data):
        return sum(data[1:], data[0]).magnitude

    @staticmethod
    def part_02(data):
        return max((x + y).magnitude for x, y in itertools.permutations(data, 2))
