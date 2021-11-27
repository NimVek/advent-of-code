import re


class Ingredient:
    pass


class Race:
    def __init__(self):
        self.stable = []

    def leader(self, time):
        result = []
        max_distance = -1
        for i in self.stable:
            distance = i.distance(time)
            if distance > max_distance:
                max_distance = distance
                result = [i]
            elif distance == max_distance:
                result.append(i)
        return result


import pprint


def parse(string):
    for line in string.splitlines():
        pprint.pprint(line)
        pprint.pprint(line.split(":"))
        name, properties = line.split(":")
        ingredient = {}
        for prop in properties.strip().split(","):
            name, value = prop.strip().split()
            ingredient[name] = int(value)
        yield ingredient


import functools
import itertools
import sys


MAX_SPOON = 100


def valuate_one(cookie):
    del cookie["calories"]
    result = 1
    for i in cookie.values():
        if i < 0:
            result = 0
        else:
            result *= i
    return result


def valuate_two(cookie):
    if cookie["calories"] == 500:
        return valuate_one(cookie)
    else:
        return -1


def iterate(ingredients, spoons, func):
    result = 0
    for i in range(0, MAX_SPOON - sum(spoons) + 1):
        tmp = spoons + [i]
        if len(ingredients) > len(tmp):
            result = max(result, iterate(ingredients, tmp, func))
        else:
            cookie = {key: 0 for key in ingredients[0].keys()}
            for c, ingredient in zip(tmp, ingredients):
                for key, value in ingredient.items():
                    cookie[key] += c * value
            result = max(result, func(cookie))
    return result


def solution(string, func):
    ingredients = list(parse(string))
    return iterate(ingredients, [], func)


one = functools.partial(solution, func=valuate_one)
two = functools.partial(solution, func=valuate_two)
