def parse(string):
    for line in string.splitlines():
        yield int(line)


def fuel(mass):
    return (mass // 3) - 2


def fuelfuel(mass):
    result = 0
    n = mass
    while n > 0:
        n = max(fuel(n), 0)
        result += n
    return result


def solution(string, func):
    return sum(map(func, parse(string)))


import functools


one = functools.partial(solution, func=fuel)
two = functools.partial(solution, func=fuelfuel)
