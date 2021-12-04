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


class Board:
    def __init__(self, tablet):
        self._tablet = tablet

    def mark(self, number):
        for r, row in enumerate(self._tablet):
            for c, item in enumerate(row):
                if item == number:
                    self._tablet[r][c] = -1
                    return self._bingo(r, c)
        return False

    def _bingo(self, row, column):
        if sum(self._tablet[row]) == -5:
            return True
        if sum(row[column] for row in self._tablet) == -5:
            return True
        return False

    def bingo(self):
        for x in range(len(self._tablet)):
            if self._bingo(x, x):
                return True
        return False

    def sums(self):
        return sum(sum(filter(lambda x: x != -1, row)) for row in self._tablet)


def parse(string):
    numbers, *boards = preparse(string)
    numbers = map(int, numbers.split(","))
    boards = [Board([list(map(int, f.split())) for f in x]) for x in boards]
    return (numbers, boards)


def one(string):
    numbers, boards = parse(string)
    for number in numbers:
        for board in boards:
            if board.mark(number):
                return board.sums() * number


def two(string):
    numbers, boards = parse(string)
    for number in numbers:
        for board in boards[:]:
            if board.mark(number):
                if len(boards) > 1:
                    boards.remove(board)
                else:
                    return board.sums() * number
