import collections.abc
import enum
import functools


class Turn(enum.IntEnum):
    LEFT = -1
    RIGHT = 1
    L = -1
    R = 1


class Direction(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Vector(tuple):
    def __new__(cls, *args):
        if isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __add__(self, other):
        return Vector(map(sum, zip(self, other)))

    def norm(self, order):
        return sum(abs(i) ** order for i in self) ** (1.0 / order)


class Navigator:
    DIRECTIONS = [Vector(1, 0), Vector(0, 1), Vector(-1, 0), Vector(0, -1)]

    def __init__(self):
        self.location = Vector(0, 0)
        self.direction = Direction.NORTH

    def turn(self, turn):
        self.direction += turn
        self.direction %= len(Navigator.DIRECTIONS)

    def steps(self, blocks):
        for _ in range(blocks):
            self.location += Navigator.DIRECTIONS[self.direction]
            yield self.location

    def walk(self, instructions):
        for turn, blocks in instructions:
            self.turn(turn)
            yield from self.steps(blocks)


class TwiceNavigator(Navigator):
    def walk(self, instructions):
        steps = set()
        for step in super().walk(instructions):
            yield step
            if step in steps:
                break
            steps.add(step)


def parse(string):
    for i in string.split(","):
        i = i.strip()
        yield (getattr(Turn, i[0]), int(i[1:]))


def solution(string, navigator):
    n = navigator()
    for last in n.walk(parse(string)):
        pass
    return int(last.norm(1))


one = functools.partial(solution, navigator=Navigator)
two = functools.partial(solution, navigator=TwiceNavigator)
