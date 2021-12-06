import collections.abc
import itertools


def simplify(item):
    if isinstance(item, collections.abc.Iterable) and not isinstance(item, str):
        item = list(item)
        if len(item) == 1:
            return item[0]
    return item


def preparse(string):
    result = [
        simplify(v)
        for k, v in itertools.groupby(string.splitlines(), lambda x: x.strip() != "")
        if k
    ]
    return simplify(result)


def parse(string):
    return map(int, string.split(","))


import collections


def solution(string, days):
    population = collections.defaultdict(int)
    for timer in parse(string):
        population[timer] += 1
    for _ in range(days):
        fishes = collections.defaultdict(int)
        for timer, fish in population.items():
            timer -= 1
            if timer < 0:
                fishes[8] = fish
                fishes[6] += fish
            else:
                fishes[timer] += fish
        population = fishes
    return sum(population.values())


import functools


one = functools.partial(solution, days=80)
two = functools.partial(solution, days=256)
