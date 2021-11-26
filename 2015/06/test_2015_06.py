import pytest
import solution_2015_06 as solution


def test_one():
    instructions = [
        "turn on 0,0 through 999,999",
        "toggle 0,0 through 999,0",
        "turn off 499,499 through 500,500",
    ]
    assert solution.one("\n".join(instructions)) == 998996


def test_two():
    instructions = ["turn on 0,0 through 0,0", "toggle 0,0 through 999,999"]
    assert solution.two("\n".join(instructions)) == 2000001
