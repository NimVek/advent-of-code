import functools
import re

from pydantic.dataclasses import dataclass

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass
class Policy:
    low: int
    high: int
    letter: str
    password: str


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(
            Policy(
                low=match["low"],
                high=match["high"],
                letter=match["letter"],
                password=match["password"],
            )
            for match in (
                re.fullmatch(
                    r"(?P<low>\d+)-(?P<high>\d+) (?P<letter>\w): (?P<password>\w+)",
                    line,
                )
                for line in data
            )
        )

    @staticmethod
    def sled_rental(policy):
        return policy.low <= policy.password.count(policy.letter) <= policy.high

    @staticmethod
    def toboggan(policy):
        return (policy.password[policy.low - 1] == policy.letter) ^ (
            policy.password[policy.high - 1] == policy.letter
        )

    @staticmethod
    def generic(data, validation):
        return sum(validation(policy) for policy in data)

    part_01 = functools.partial(generic, validation=sled_rental)
    part_02 = functools.partial(generic, validation=toboggan)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
