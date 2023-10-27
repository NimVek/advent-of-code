from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Node:
    children: tuple["Node", ...]
    metadata: tuple[int, ...]

    @classmethod
    def from_iterable(cls, iterable) -> "Node":
        it = iter(iterable)
        count_children = next(it)
        count_metadata = next(it)
        children = tuple(cls.from_iterable(it) for _ in range(count_children))
        metadata = tuple(next(it) for _ in range(count_metadata))
        return cls(children=children, metadata=metadata)

    @property
    def sum_metadata(self) -> int:
        return sum(c.sum_metadata for c in self.children) + sum(self.metadata)

    @property
    def value(self) -> int:
        if not self.children:
            return sum(self.metadata)
        return sum(
            self.children[i - 1].value
            for i in self.metadata
            if 1 <= i <= len(self.children)
        )


class Solution(SolutionBase):
    @staticmethod
    def prepare(data) -> Node:
        return Node.from_iterable(map(int, data.split()))

    @staticmethod
    def part_01(root: Node) -> int:
        return root.sum_metadata

    @staticmethod
    def part_02(root: Node) -> int:
        return root.value


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
