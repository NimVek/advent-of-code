import collections
import functools

from aoc.lib.solution import SolutionBase

import logging


__all__ = ["Solution"]
__log__ = logging.getLogger(__name__)


class Polymerization:
    def __init__(self, rules):
        self.rules = {(a, b): ((a, z), (z, b)) for (a, b), z in rules.items()}

    def insertion(self, pairs):
        result = collections.defaultdict(int)
        for pair, quantity in pairs.items():
            rule = self.rules.get(pair, (pair,))
            for new_pair in rule:
                result[new_pair] += quantity
        return result


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        template, rules = data
        rules = dict(rule.split(" -> ") for rule in rules)
        return template, rules

    @staticmethod
    def generic(data, steps):
        template, rules = data
        pairs = collections.Counter(zip(template, template[1:]))
        polymerization = Polymerization(rules)
        for _ in range(steps):
            pairs = polymerization.insertion(pairs)
        elements = collections.defaultdict(int)
        for (element, _), quantity in pairs.items():
            elements[element] += quantity
        elements[template[-1]] += 1
        return max(elements.values()) - min(elements.values())

    part_01 = functools.partialmethod(generic, steps=10)
    part_02 = functools.partialmethod(generic, steps=40)
