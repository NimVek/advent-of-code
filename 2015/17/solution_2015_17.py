import itertools
import re


def parse(string):
    for line in string.splitlines():
        yield int(line.strip())


import functools
import sys


MAX_SPOON = 150


def iterate_one(s, container):
    if s == 150:
        return 1
    if s > 150:
        return 0
    if container:
        a, *e = container
        result = iterate_one(s, e)
        result += iterate_one(s + a, e)
        return result
    return 0


def one(string):
    container = list(parse(string))
    container.sort(reverse=True)
    result = 0
    result = iterate_one(0, container)
    return result


def iterate_two(s, container):
    if sum(s) == 150:
        return (len(s), 1)
    if sum(s) > 150:
        return None
    if container:
        a, *e = container
        result = iterate_two(s, e) or (sys.maxsize, 0)
        tmp = iterate_two(s + [a], e) or (sys.maxsize, 0)
        if result[0] == tmp[0]:
            result = (result[0], result[1] + tmp[1])
        return result if result[0] <= tmp[0] else tmp
    return None


def two(string):
    container = list(parse(string))
    container.sort(reverse=True)
    result = iterate_two([], container)
    return result[1]
