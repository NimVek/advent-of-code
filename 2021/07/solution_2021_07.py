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


import math
import statistics


def triangle(n):
    return math.comb(int(abs(n)) + 1, 2)


def triangle_center(crabs):
    mean = statistics.mean(crabs)
    bigger = sum(c > mean for c in crabs)
    return mean + (2 * bigger - len(crabs)) / (2 * len(crabs))


def solution(string, target, distance):
    crabs = list(parse(preparse(string)))
    target = round(target(crabs))
    return sum(map(distance, map(lambda x: x - target, crabs)))


import functools


one = functools.partial(solution, target=statistics.median, distance=abs)
two = functools.partial(solution, target=triangle_center, distance=triangle)
