import importlib
import logging
import pprint
import sys

import aoc.lib.parse


logger = logging.getLogger(__name__)


def cmd_run(args):
    sys.path.append(str(args.current))

    with open(args.current / "input") as f:
        data = f.read().strip()
    data = aoc.lib.parse.parse_blocks(data)
    solution = importlib.import_module("solution")

    part = 1 if args.part == "one" else 2
    pprint.pprint(solution.Solution.solve(part, data))


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
