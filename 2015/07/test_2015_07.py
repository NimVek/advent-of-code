import pytest
import solution_2015_07 as solution


@pytest.mark.parametrize(
    ("wire", "value"),
    [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ],
)
def test_one(wire, value):
    instructions = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    wires = solution.Wires()
    solution.iterate(solution.parse("\n".join(instructions)), wires)
    assert wires[wire] == value
