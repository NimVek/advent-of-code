import collections
import itertools
import logging

from aoc.lib.solution import SolutionBase


__all__ = ["Solution"]
logger = logging.getLogger(__name__)


class Dice:
    def __init__(self, sides=100, quantity=3):
        self.quantity = quantity
        self.rolls = 0
        self.throw = itertools.cycle(range(1, sides + 1)).__next__

    def roll(self):
        self.rolls += 3
        return sum(self.throw() for _ in range(self.quantity))


class Player:
    def __init__(self, position, dice, boardsize=10):
        self.position = position - 1
        self.dice = dice
        self.boardsize = boardsize
        self.score = 0

    def roll_and_win(self, winning_score=1000):
        self.position = (self.position + self.dice.roll()) % self.boardsize
        self.score += self.position + 1
        return self.score >= winning_score


class QuantumDice:  # noqa: SIM119
    def __init__(self, sides=3, quantity=3):
        values = range(1, sides + 1)
        dice = (values,) * quantity
        self.rolls = collections.Counter(map(sum, itertools.product(*dice)))


class QuantumPlayer:
    def __init__(self, position, dice, boardsize=10):
        self.universes = {(position - 1, 0): 1}
        self.dice = dice
        self.boardsize = boardsize
        self.winning_universes = 0

    def roll(self, opponent, winning_score=21):
        copies = collections.defaultdict(int)
        open_universes = opponent.open_universes
        for (position, score), quantity in self.universes.items():
            for value, possibilities in self.dice.rolls.items():
                new_position = (position + value) % self.boardsize
                new_score = score + new_position + 1
                new_quantity = quantity * possibilities
                if new_score >= winning_score:
                    self.winning_universes += new_quantity * open_universes
                else:
                    copies[(new_position, new_score)] += new_quantity

        self.universes = copies

    @property
    def open_universes(self):
        return sum(self.universes.values())


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return map(int, (line.split(" ")[-1] for line in data))

    @staticmethod
    def part_01(data):
        dice = Dice()
        players = tuple(Player(start, dice) for start in data)
        player = 0
        while not players[player].roll_and_win():
            player = (player + 1) % 2
        return min(player.score for player in players) * dice.rolls

    @staticmethod
    def part_02(data):
        dice = QuantumDice()
        players = tuple(QuantumPlayer(start, dice) for start in data)
        player = 0
        while players[player].universes:
            players[player].roll(players[(player + 1) % 2])
            player = (player + 1) % 2
        return max(player.winning_universes for player in players)
