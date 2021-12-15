import collections
import functools


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


def parse(data):
    template, rules = data
    rules = [rule.split(" -> ") for rule in rules]
    rules = {a: z for (a, z) in rules}
    return template, rules


def solution(data, steps):
    template, rules = parse(data)
    pairs = collections.Counter(zip(template, template[1:]))
    polymerization = Polymerization(rules)
    for _ in range(steps):
        pairs = polymerization.insertion(pairs)
    elements = collections.defaultdict(int)
    for (element, _), quantity in pairs.items():
        elements[element] += quantity
    elements[template[-1]] += 1
    return max(elements.values()) - min(elements.values())


one = functools.partial(solution, steps=10)
two = functools.partial(solution, steps=40)
