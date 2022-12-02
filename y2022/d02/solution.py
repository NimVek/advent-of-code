import collections
import enum
import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Shape(enum.IntEnum):
    ROCK = A = X = 0
    PAPER = B = Y = 1
    SCISSORS = C = Z = 2

    @property
    def score(self):
        return self + 1

    def outcome(self, opponent):
        return Outcome((self - opponent + 1) % len(Shape))


class Outcome(enum.IntEnum):
    LOOSE = X = 0
    DRAW = Y = 1
    WIN = Z = 2

    @property
    def score(self):
        return self * 3

    def response(self, opponent):
        return Shape((self + opponent - 1) % len(Shape))


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def generic(rounds, strategy=None):
        rounds = collections.Counter(rounds)
        __log__.debug(rounds)
        return sum(strategy(_round) * _count for _round, _count in rounds.items())

    @staticmethod
    def strategy_response(_round):
        opponent, own = _round.split()
        opponent = Shape[opponent]
        own = Shape[own]

        return own.score + own.outcome(opponent).score

    @staticmethod
    def strategy_outcome(_round):
        opponent, outcome = _round.split()
        opponent = Shape[opponent]
        outcome = Outcome[outcome]

        return outcome.response(opponent).score + outcome.score

    part_01 = functools.partial(generic, strategy=strategy_response)
    part_02 = functools.partial(generic, strategy=strategy_outcome)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
