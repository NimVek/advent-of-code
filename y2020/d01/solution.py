import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return tuple(int(x) for x in data)

    @staticmethod
    def product_if_total(numbers, total, quantity):
        if quantity == 1:
            if total in numbers:
                return total
        else:
            while numbers:
                number, *numbers = numbers
                result = Solution.product_if_total(
                    numbers, total - number, quantity - 1
                )
                if result:
                    return result * number

    part_01 = functools.partial(product_if_total, total=2020, quantity=2)
    part_02 = functools.partial(product_if_total, total=2020, quantity=3)


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
