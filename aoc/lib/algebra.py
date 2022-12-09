import collections.abc
import math

import logging


__log__ = logging.getLogger(__name__)


class Vector(tuple):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __add__(self, other):
        return self.__class__(map(sum, zip(self, other)))

    def __sub__(self, other):
        return self.__class__(x - y for x, y in zip(self, other))

    def norm(self, order):
        return sum(abs(i) ** order for i in self) ** (1.0 / order)

    def dot(self, other):
        return sum(math.prod(prod) for prod in zip(self, other))


class Matrix(tuple):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], collections.abc.Iterable):
            args = args[0]
        return super().__new__(cls, args)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(*map(other.dot, self))
        return NotImplemented
