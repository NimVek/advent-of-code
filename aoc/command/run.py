import collections.abc
import importlib
import itertools
import pprint
import sys


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


def cmd_run(args):
    sys.path.append(str(args.current))

    with open(args.current / "input", "r") as f:
        input = f.read().strip()
    input = preparse(input)
    solution = importlib.import_module(f"solution")

    part = 1 if args.part == "one" else 2
    pprint.pprint(solution.Solution.solve(part, input))


def cmd_answer(args):
    level = 1
    if args.part == "two":
        level = 2
    pprint.pprint(args.api.answer(args.year, args.day, level, args.answer))


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("run")
    parser.set_defaults(func=cmd_run)

    parser.add_argument(
        "part",
        default="one",
        type=str,
        choices=["one", "two"],
    )

    parser = parent_parser.add_parser("answer")
    parser.set_defaults(func=cmd_answer)

    parser.add_argument(
        "part",
        default="one",
        type=str,
        choices=["one", "two"],
    )

    parser.add_argument(
        "answer",
        default="one",
        type=str,
    )
