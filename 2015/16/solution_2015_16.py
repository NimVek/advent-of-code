import pprint


def parse(string):
    for line in string.splitlines():
        pprint.pprint((line, line.split(":")))
        name, properties = line.split(":", 1)
        _, idx = name.strip().split()
        ingredient = {"idx": int(idx)}
        for prop in properties.strip().split(","):
            name, value = prop.strip().split(":")
            ingredient[name.strip()] = int(value.strip())
        yield ingredient


import functools


MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

equal = lambda a, b: a == b
lesser = lambda a, b: a > b
greater = lambda a, b: a < b

COMPERATOR_ONE = {
    "children": equal,
    "cats": equal,
    "samoyeds": equal,
    "pomeranians": equal,
    "akitas": equal,
    "vizslas": equal,
    "goldfish": equal,
    "trees": equal,
    "cars": equal,
    "perfumes": equal,
}

COMPERATOR_TWO = {
    "children": equal,
    "cats": greater,
    "samoyeds": equal,
    "pomeranians": lesser,
    "akitas": equal,
    "vizslas": equal,
    "goldfish": lesser,
    "trees": greater,
    "cars": equal,
    "perfumes": equal,
}


def solution(string, comperator):
    for aunt in parse(string):
        result = True
        for key, value in aunt.items():
            if key == "idx":
                continue
            if not comperator[key](MFCSAM[key], value):
                result = False
        if result:
            return aunt["idx"]


one = functools.partial(solution, comperator=COMPERATOR_ONE)
two = functools.partial(solution, comperator=COMPERATOR_TWO)
