import collections.abc
import dataclasses

from dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class FSNode:
    name: str


@dataclass
class FSFile(FSNode):
    size: int


@dataclass
class FSDirectory(FSNode, collections.abc.Mapping):
    children: dict[str, FSNode] = dataclasses.field(default_factory=dict, init=False)
    parent: "FSDirectory" = dataclasses.field(default=None, repr=False)

    def __post_init__(self):
        self.children = {}

    def iterate(self, typ):
        if isinstance(self, typ):
            yield self
        for child in self.children.values():
            if isinstance(child, FSDirectory):
                yield from child.iterate(typ)
            else:
                if isinstance(child, typ):
                    yield child

    def __getitem__(self, key):
        return self.children[key]

    def __iter__(self):
        return iter(self.children)

    def __len__(self):
        return len(self.children)

    def add(self, node):
        self.children[node.name] = node

    @property
    def size(self):
        return sum(child.size for child in self.children.values())


class Solution(SolutionBase):
    @staticmethod
    def prepare(listing):
        root = FSDirectory(name="/")
        current_directory = None
        for line in listing:
            if line[0] == "$":
                _, cmd, *argv = line.split()
                if cmd == "cd":
                    if argv[0] == "/":
                        current_directory = root
                    elif argv[0] == "..":
                        current_directory = current_directory.parent
                    else:
                        current_directory = current_directory[argv[0]]
            else:
                size, name = line.split()
                if size == "dir":
                    current_directory.add(
                        FSDirectory(name=name, parent=current_directory)
                    )
                else:
                    current_directory.add(FSFile(name=name, size=int(size)))

        return root

    @staticmethod
    def part_01(root):
        return sum(
            child.size for child in root.iterate(FSDirectory) if child.size <= 100000
        )

    @staticmethod
    def part_02(root):
        needed = 30000000 - (70000000 - root.size)
        return min(
            child.size for child in root.iterate(FSDirectory) if child.size >= needed
        )


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
