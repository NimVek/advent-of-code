import contextlib
import re


class Wire:
    def _value(self, variable):
        value = None
        with contextlib.suppress(ValueError):
            value = int(variable)
        if value is None:
            value = self.wires[variable]
        return value


class Int(Wire):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self._value(self.value)


class And(Wire):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __int__(self):
        return self._value(self.left) & self._value(self.right)


class Or(Wire):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __int__(self):
        return self._value(self.left) | self._value(self.right)


class LShift(Wire):
    def __init__(self, left, right):
        self.left = left
        self.right = int(right)

    def __int__(self):
        return self._value(self.left) << self._value(self.right)


class RShift(Wire):
    def __init__(self, left, right):
        self.left = left
        self.right = int(right)

    def __int__(self):
        return self._value(self.left) >> self._value(self.right)


class Not(Wire):
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return 0xFFFF - self._value(self.value)


class Wires:
    def __init__(self):
        self.wires = {}

    def __setitem__(self, key, value):
        value.wires = self
        self.wires[key] = value

    def __getitem__(self, key):
        value = self.wires[key]
        if not isinstance(value, int):
            value = int(value)
            self.wires[key] = value
        return value


def parse(string):
    for command in string.splitlines():
        match = re.match(r"NOT\s+(?P<value>\w+)\s+->\s+(?P<wire>\w+)", command)
        if match:
            yield {
                "command": "NOT",
                "arguments": (match.group("value"),),
                "wire": match.group("wire"),
            }
        else:
            match = re.match(
                r"(?P<left>\w+)\s+(?P<command>AND|OR|LSHIFT|RSHIFT)\s+(?P<right>\w+)\s+->\s+(?P<wire>\w+)",
                command,
            )
            if match:
                yield {
                    "command": match.group("command"),
                    "arguments": (match.group("left"), match.group("right")),
                    "wire": match.group("wire"),
                }
            else:
                match = re.match(r"(?P<value>\w+)\s+->\s+(?P<wire>\w+)", command)
                if match:
                    yield {
                        "command": "INT",
                        "arguments": (match.group("value"),),
                        "wire": match.group("wire"),
                    }


INSTRUCTION = {
    "INT": Int,
    "AND": And,
    "OR": Or,
    "LSHIFT": LShift,
    "RSHIFT": RShift,
    "NOT": Not,
}


def iterate(instructions, wires):
    for instruction in instructions:
        cls = INSTRUCTION[instruction["command"]]
        wires[instruction["wire"]] = cls(*(instruction["arguments"]))


def one(string):
    wires = Wires()
    iterate(parse(string), wires)
    return wires["a"]


def two(string):
    wires = Wires()
    iterate(parse(string), wires)
    a = wires["a"]
    wires = Wires()
    iterate(parse(string), wires)
    wires["b"] = Int(a)
    return wires["a"]
