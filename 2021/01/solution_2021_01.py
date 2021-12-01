def parse(string):
    return list(map(int, string.splitlines()))


def solution(string, _range):
    measurements = parse(string)
    return sum(
        map(lambda deep: deep[0] < deep[1], zip(measurements, measurements[_range:]))
    )


import functools


one = functools.partial(solution, _range=1)
two = functools.partial(solution, _range=3)
