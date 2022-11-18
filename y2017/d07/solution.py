import re

from dataclasses import dataclass
from functools import cached_property

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Program:
    name: str
    weight: int
    disc: tuple

    @cached_property
    def tower_weight(self):
        return self.weight + sum(program.tower_weight for program in self)

    def __getitem__(self, idx):
        return self.library[self.disc[idx]]

    def __len__(self):
        return len(self.disc)

    def balance(self, difference=0):
        disc = sorted(self, key=lambda x: x.tower_weight)
        __log__.debug(disc)
        if disc[-1].tower_weight != disc[-2].tower_weight:
            disc.reverse()

        unbalanced = disc[0].tower_weight - disc[1].tower_weight
        if unbalanced != 0:
            return disc[0].balance(unbalanced)
        return self.weight - difference


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        library = {}
        p = re.compile(r"(?P<name>\w+) \((?P<weight>\d+)\)( -> (?P<disc>\w+(, \w+)*))?")
        for line in data:
            m = p.match(line)
            disc = m.group("disc")
            disc = tuple(disc.split(", ")) if disc else ()
            program = Program(m.group("name"), int(m.group("weight")), disc)
            program.library = library
            library[program.name] = program
            __log__.debug(program)
        return library

    @staticmethod
    def part_01(data):
        result = set(data)
        __log__.debug(result)
        for program in data.values():
            result -= set(program.disc)
            __log__.debug(result)
        return tuple(result)[0]

    @staticmethod
    def part_02(data):
        bottom = Solution.part_01(data)
        return data[bottom].balance()


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
