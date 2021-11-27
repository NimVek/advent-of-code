import functools
import json


def sumup(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum([sumup(i) for i in data])
    elif isinstance(data, dict):
        return sum([sumup(i) for i in data.values()])
    return 0


def nored(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum([nored(i) for i in data])
    elif isinstance(data, dict):
        values = data.values()
        if "red" not in values:
            return sum([nored(i) for i in values])
    return 0


def solution(string, func):
    data = json.loads(string)
    return func(data)


one = functools.partial(solution, func=sumup)
two = functools.partial(solution, func=nored)
