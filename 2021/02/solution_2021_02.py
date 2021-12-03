class SimpleSubmarine:
    def __init__(self):
        self.horizontal = 0
        self.__depth = 0

    @property
    def depth(self):
        return self.__depth

    def forward(self, i):
        self.horizontal += i

    def up(self, i):
        self.__depth -= i

    def down(self, i):
        self.__depth += i

    def distance(self):
        return self.horizontal * self.depth


class ComplexSubmarine(SimpleSubmarine):
    def __init__(self):
        super().__init__()
        self.__depth = 0

    @property
    def aim(self):
        return super().depth

    @property
    def depth(self):
        return self.__depth

    def forward(self, i):
        super().forward(i)
        self.__depth += self.aim * i


def parse(string):
    for line in string.splitlines():
        direction, _count = line.split()
        yield (direction, int(_count))


def solution(string, submarine):
    for direction, _count in parse(string):
        getattr(submarine, direction)(_count)
    return submarine.distance()


import functools


one = functools.partial(solution, submarine=SimpleSubmarine())
two = functools.partial(solution, submarine=ComplexSubmarine())
