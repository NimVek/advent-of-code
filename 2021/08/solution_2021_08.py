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


class Segments:
    def __init__(self, pattern):
        digits = {}
        pattern = [frozenset(p) for p in pattern]
        for p in pattern:
            if len(p) == 2:
                digits[1] = p
            elif len(p) == 3:
                digits[7] = p
            elif len(p) == 4:
                digits[4] = p
            elif len(p) == 7:
                digits[8] = p
        for p in pattern:
            if len(p) == 5:
                if len(p & digits[1]) == 2:
                    digits[3] = p
                elif len(p & digits[4]) == 3:
                    digits[5] = p
                else:
                    digits[2] = p
            elif len(p) == 6:
                if len(p & digits[4]) == 4:
                    digits[9] = p
                elif len(p & digits[7]) == 3:
                    digits[0] = p
                else:
                    digits[6] = p
        self.digits = {v: str(k) for k, v in digits.items()}

    def display(self, digit):
        return self.digits[frozenset(digit)]


def parse(string):
    for line in string:
        pattern, digits = line.split("|")
        yield (pattern.split(), digits.split())


import collections


def one(string):
    digits = (digit for pattern, digit in parse(preparse(string)))
    digits = map(len, itertools.chain(*digits))
    digits = collections.Counter(digits)
    return digits[2] + digits[3] + digits[4] + digits[7]


def two(string):
    result = 0
    for pattern, digits in parse(preparse(string)):
        segment = Segments(pattern)
        digits = map(segment.display, digits)
        result += int("".join(digits))
    return result
