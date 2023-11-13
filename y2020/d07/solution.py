import functools

from dataclasses import dataclass, field

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Bag:
    color: str
    content: dict[str, int]
    rules: dict[str, "Bag"] = field(repr=False)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.color == other
        if isinstance(other, Bag):
            return self.color == other.color
        return NotImplemented

    def __hash__(self):
        return super().__hash__()

    @functools.cache
    def __contains__(self, item):
        return item in self.content or any(
            item in self.rules[color] for color in self.content
        )

    @functools.cache
    def __len__(self):
        return 1 + sum(
            _count * len(self.rules[color]) for color, _count in self.content.items()
        )


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        rules = {}
        for line in data:
            color, ingredients = line.split(" bags contain ")
            content = {}
            if not ingredients.startswith("no"):
                for bag in ingredients.split(", "):
                    _count, *subcolor, _ = bag.split()
                    content[" ".join(subcolor)] = int(_count)
            rules[color] = Bag(color=color, content=content, rules=rules)
        return rules

    @staticmethod
    def part_01(data):
        return sum(1 for bag in data.values() if "shiny gold" in bag)

    @staticmethod
    def part_02(data):
        return len(data["shiny gold"]) - 1


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
