import itertools
import math

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Data:
    instructions: str
    nodes: dict[str, dict[str, str]]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return Data(
            instructions=data[0],
            nodes={
                node[0]: {"L": node[2][1:-1], "R": node[3][:-1]}
                for node in (node.split() for node in data[1])
            },
        )

    @staticmethod
    def steps(start, end, instructions, nodes):
        node = start
        for idx, instruction in enumerate(itertools.cycle(instructions), start=1):
            node = nodes[node][instruction]
            if end(node):
                return idx

    @staticmethod
    def part_01(data):
        return Solution.steps(
            "AAA", lambda x: x == "ZZZ", data.instructions, data.nodes
        )

    @staticmethod
    def part_02(data):
        return math.lcm(
            *(
                Solution.steps(
                    node, lambda x: x[-1] == "Z", data.instructions, data.nodes
                )
                for node in data.nodes
                if node[-1] == "A"
            )
        )


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
