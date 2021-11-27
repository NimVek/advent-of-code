import re


class Reindeer:
    def __init__(self, speed, fly, rest):
        self.speed = speed
        self.fly = fly
        self.rest = rest
        self.leads = 0

    def distance(self, time):
        cycles = time // (self.fly + self.rest)
        result = cycles * self.speed * self.fly
        result += self.speed * min(self.fly, time % (self.fly + self.rest))
        return result


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
    for distance in string.splitlines():
        match = re.match(
            r"(?P<who>\w+)\s+can\s+fly\s+(?P<speed>\d+)\s+km/s\s+for\s+(?P<fly>\d+)\s+seconds,\s+but\s+then\s+must\s+rest\s+for\s+(?P<rest>\d+)\s+seconds\.",
            distance,
        )
        if match:
            yield Reindeer(
                int(match.group("speed")),
                int(match.group("fly")),
                int(match.group("rest")),
            )


import functools
import itertools
import sys


MAX_TIME = 2503


def one(string):
    race = Race()
    race.stable = list(parse(string))
    return race.leader(MAX_TIME)[0].distance(MAX_TIME)


def two(string):
    race = Race()
    race.stable = list(parse(string))
    for i in range(1, MAX_TIME + 1):
        for deer in race.leader(i):
            deer.leads += 1
    return max([i.leads for i in race.stable])
