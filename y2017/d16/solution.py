import functools

from dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Spin:
    x: int

    def __call__(self, line):
        return line[-self.x :] + line[: -self.x]


@dataclass
class Exchange:
    a: int
    b: int

    def __call__(self, line):
        line[self.a], line[self.b] = line[self.b], line[self.a]
        return line


@dataclass
class Partner:
    a: str
    b: str

    def __call__(self, line):
        a, b = map(line.index, (self.a, self.b))
        line[a], line[b] = line[b], line[a]
        return line


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        dance = []
        for move in data.split(","):
            if move[0] == "s":
                dance.append(Spin(int(move[1:])))
            elif move[0] == "x":
                dance.append(Exchange(*map(int, move[1:].split("/"))))
            elif move[0] == "p":
                dance.append(Partner(*move[1:].split("/")))
        return tuple(dance)

    @staticmethod
    def generic(dance, times):
        line = "abcdefghijklmnop"
        seen = []
        for i in range(times):
            if line in seen:
                return seen[times % i]
            seen.append(line)
            line = list(line)
            for move in dance:
                line = move(line)
            line = "".join(line)
        return line

    part_01 = functools.partial(generic, times=1)
    part_02 = functools.partial(generic, times=1000000000)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
