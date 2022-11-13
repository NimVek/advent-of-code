import importlib
import io
import pprint
import pstats
import sys

import aoc.lib.parse
import aoc.lib.profile

import logging


__log__ = logging.getLogger(__name__)


def run_parameter(path, part):
    sys.path.append(str(path))

    with open(path / "input") as f:
        data = f.read().strip()
    data = aoc.lib.parse.parse_blocks(data)
    solution = importlib.import_module("solution")
    data = solution.Solution.prepare(data)

    part = 1 if part == "one" else 2
    func = getattr(solution.Solution, f"part_{part:02}")
    return (func, data)


def run(path, part):
    func, data = run_parameter(path, part)
    return func(data)


def cmd_run(args):
    func, data = run_parameter(args.current, args.part)
    func = aoc.lib.profile.profile(func)
    result = func(data)
    s = io.StringIO()
    ps = pstats.Stats(func.__profile__, stream=s).strip_dirs().sort_stats("cumulative")
    ps.print_stats(30)
    print(s.getvalue())
    pprint.pprint(result)


def cmd_answer(args):
    level = 1
    if args.part == "two":
        level = 2
    answer = args.answer or run(args.current, args.part)
    pprint.pprint(args.api.answer(args.year, args.day, level, answer))


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
        nargs="?",
        type=str,
    )
