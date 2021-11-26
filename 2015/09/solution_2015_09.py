import re


class Distance:
    def __init__(self):
        self._distance = {}

    def add(self, p1, p2, distance):
        if p1 not in self._distance:
            self._distance[p1] = {}
        self._distance[p1][p2] = distance
        if p2 not in self._distance:
            self._distance[p2] = {}
        self._distance[p2][p1] = distance

    def distance(self, p1, p2):
        return self._distance[p1][p2]

    def places(self):
        return self._distance.keys()


def parse(string):
    for distance in string.splitlines():
        match = re.match(
            r"(?P<from>\w+)\s+to\s+(?P<to>\w+)\s+=\s+(?P<distance>[0-9]+)",
            distance,
        )
        if match:
            yield {
                "from": match.group("from"),
                "to": match.group("to"),
                "distance": int(match.group("distance")),
            }


def iterate(distances, m):
    for distance in distances:
        m.add(distance["from"], distance["to"], distance["distance"])


import functools
import itertools
import sys


def solution(string, func, init):
    distance = Distance()
    iterate(parse(string), distance)
    result = init
    for route in itertools.permutations(distance.places()):
        length = 0
        for start, end in zip(route[:-1], route[1:]):
            length += distance.distance(start, end)
        result = func(result, length)
    return result


one = functools.partial(solution, func=min, init=sys.maxsize)
two = functools.partial(solution, func=max, init=0)
