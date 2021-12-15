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


logger = logging.getLogger(__name__)


def prepare(data):
    return data


def one(data):
    raise NotImplementedError


def two(data):
    raise NotImplementedError
"""
            f.write(content)

    test = args.current / "test.py"
    if not test.is_file():
        with open(test, "w") as f:
            content = """import pytest

from . import solution


@pytest.mark.parametrize(
    ("part", "answer"),
    [
        ("one", None),
        ("two", None),
    ],
)
def test(part, answer):
    data = None

    assert getattr(solution, part)(data) == answer
"""
            f.write(content)

    readme = args.current / "README.md"
    if not readme.is_file():
        with open(readme, "w") as f:
            f.write(args.api.mission(args.year, args.day))

    input = args.current / "input"
    if not input.is_file():
        with open(input, "w") as f:
            f.write(args.api.input(args.year, args.day))


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("init")
    parser.set_defaults(func=cmd_init)
