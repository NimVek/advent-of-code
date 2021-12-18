def cmd_init(args):
    args.current.mkdir(parents=True, exist_ok=True)

    init = args.current / "__init__.py"
    if not init.is_file():
        with open(init, "w") as f:
            pass

    solution = args.current / "solution.py"
    if not solution.is_file():
        with open(solution, "w") as f:
            content = """import logging

from aoc.lib.solution import SolutionBase


__all__ = ["Solution"]
logger = logging.getLogger(__name__)


class Solution(SolutionBase):
    @staticmethod
    def prepare(data):
        return data

    @staticmethod
    def part_01(data):
        raise NotImplementedError

    @staticmethod
    def part_02(data):
        raise NotImplementedError
"""
            f.write(content)

    test = args.current / "test.py"
    if not test.is_file():
        with open(test, "w") as f:
            content = """import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("part", "answer"),
    [
        (1, None),
        (2, None),
    ],
)
def test(part, answer):
    data = None

    assert Solution.solve(part, data) == answer
"""
            f.write(content)

    readme = args.current / "README.md"
    if not readme.is_file():
        with open(readme, "w") as f:
            f.write(args.api.mission(args.year, args.day))

    data = args.current / "input"
    if not data.is_file():
        with open(data, "w") as f:
            f.write(args.api.data(args.year, args.day))


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("init")
    parser.set_defaults(func=cmd_init)
