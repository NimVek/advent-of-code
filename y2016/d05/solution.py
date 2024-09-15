import functools
import hashlib
import typing

from aoc.lib.digest import parallel
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Item(typing.NamedTuple):
    position: int
    character: str


class Syncronous:
    def __init__(self):
        self.idx = 0

    def __call__(self, item):
        result = Item(self.idx, item.digest[5])
        self.idx += 1
        return result


class Asyncronous:
    def __call__(self, item):
        return Item(int(item.digest[5], 16), item.digest[6])


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def validate(digest):
        return digest.startswith("00000")

    @staticmethod
    def generic(door_id, converter_class, length=8):
        converter = converter_class()
        result = [None] * length
        for position, character in map(
            converter, parallel(hashlib.md5, door_id, Solution.validate)
        ):
            if position < length and result[position] is None:
                result[position] = character
                if None not in result:
                    return "".join(result)
            __log__.debug(result)

    part_01 = functools.partial(generic, converter_class=Syncronous)
    part_02 = functools.partial(generic, converter_class=Asyncronous)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
