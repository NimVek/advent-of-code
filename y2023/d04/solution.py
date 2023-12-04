from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Card:
    id: int
    winning: set[int]
    numbers: set[int]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            Card(
                id=int(card[5:]),
                winning={int(number) for number in winning.split()},
                numbers={int(number) for number in numbers.split()},
            )
            for card, winning, numbers in (
                line.replace("|", ":").split(":") for line in data
            )
        )

    @staticmethod
    def part_01(data):
        return sum(int(2 ** (len(card.winning & card.numbers) - 1)) for card in data)

    @staticmethod
    def part_02(data):
        copies = [1] * len(data[0].winning)
        result = 0
        for card in data:
            _count = copies.pop(0)
            result += _count
            copies.append(1)
            for i in range(len(card.winning & card.numbers)):
                copies[i] += _count
        return result


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
