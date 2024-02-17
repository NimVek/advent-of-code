import re


class Distance:
    def __init__(self):
        self._distance = {}

    def add(self, p1, p2, distance):
        if p1 not in self._distance:
            self._distance[p1] = {}
        self._distance[p1][p2] = distance

    def distance(self, p1, p2):
        return self._distance[p1][p2]

    def places(self):
        return self._distance.keys()


def parse(string):
    for distance in string.splitlines():
        match = re.match(
            r"(?P<from>\w+)\s+would\s+(?P<how>gain|lose)\s+(?P<many>\d+)\s+happiness\s+units\s+by\s+sitting\s+next\s+to\s+(?P<to>\w+)",
            distance,
        )
        if match:
            yield {
                "from": match.group("from"),
                "to": match.group("to"),
                "happiness": int(match.group("many"))
                * (-1 if match.group("how") == "lose" else 1),
            }


def iterate(distances, m):
    for distance in distances:
        m.add(distance["from"], distance["to"], distance["happiness"])


import itertools


def calculate(distance, func, init):
    result = init
    for route in itertools.permutations(distance.places()):
        length = 0
        l = len(route)
        for i in range(0, l):
            length += distance.distance(route[i], route[(i + 1) % l])
            length += distance.distance(route[(i + 1) % l], route[i])
        result = func(result, length)
    return result


def one(string):
    distance = Distance()
    iterate(parse(string), distance)
    return calculate(distance, max, 0)


def two(string):
    distance = Distance()
    iterate(parse(string), distance)
    for i in list(distance.places()):
        distance.add("Santa", i, 0)
        distance.add(i, "Santa", 0)
    return calculate(distance, max, 0)
