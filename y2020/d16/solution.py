import collections
import functools

from dataclasses import dataclass
from math import prod

from aoc.lib.algorithms import possibilities_to_dict
from aoc.lib.sets import IntervalSet
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)

Ticket = tuple[int, ...]


@dataclass
class Input:
    rules: dict[str, IntervalSet]
    own: Ticket
    nearby: list[Ticket]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return Input(
            rules={
                field: IntervalSet(
                    *(
                        map(int, interval.split("-"))
                        for interval in value.strip().split(" or ")
                    )
                )
                for field, value in (rule.split(":") for rule in data[0])
            },
            own=tuple(map(int, data[1][1].split(","))),
            nearby=list(tuple(map(int, ticket.split(","))) for ticket in data[2][1:]),
        )

    @staticmethod
    def part_01(data):
        valid = functools.reduce(lambda a, b: a | b, data.rules.values())
        return sum(sum(x for x in ticket if x not in valid) for ticket in data.nearby)

    @staticmethod
    def part_02(data):
        valid = functools.reduce(lambda a, b: a | b, data.rules.values())
        tickets = (ticket for ticket in data.nearby if all(x in valid for x in ticket))

        investigate = collections.defaultdict(lambda: set(range(len(data.own) + 1)))
        for ticket in tickets:
            for name, values in data.rules.items():
                investigate[name] &= {
                    idx for idx, value in enumerate(ticket) if value in values
                }

        translate = possibilities_to_dict(investigate)

        return prod(
            data.own[idx]
            for name, idx in translate.items()
            if name.startswith("departure")
        )


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
