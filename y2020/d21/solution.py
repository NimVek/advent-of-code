import functools
import operator

from pydantic.dataclasses import dataclass

from aoc.lib.algorithms import possibilities_to_dict
from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


@dataclass(frozen=True)
class Food:
    ingredients: frozenset[str]
    allergens: frozenset[str]


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return frozenset(
            Food(
                ingredients=frozenset(ingredients.split()),
                allergens=frozenset(allergens.split(", ")),
            )
            for ingredients, allergens in (
                line.rstrip(")").split(" (contains ") for line in data
            )
        )

    @staticmethod
    def possibly_allergens(data):
        return {
            allergen: functools.reduce(
                operator.__and__,
                (food.ingredients for food in data if allergen in food.allergens),
            )
            for allergen in functools.reduce(
                operator.__or__, (food.allergens for food in data)
            )
        }

    @staticmethod
    def part_01(data):
        allergens = functools.reduce(
            operator.__or__, Solution.possibly_allergens(data).values()
        )
        return sum(len(food.ingredients - allergens) for food in data)

    @staticmethod
    def part_02(data):
        allergens = possibilities_to_dict(Solution.possibly_allergens(data))
        return ",".join(allergens[allergen] for allergen in sorted(allergens))


if __name__ == "__main__":
    import aoc.lib.main

    aoc.lib.main.main(Solution)
