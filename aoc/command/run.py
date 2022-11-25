import datetime
import enum
import importlib
import io
import pstats
import re
import sys

import dateparser
import termcolor

import aoc.lib.parse
import aoc.lib.profile
import aoc.misc.arguments

import logging


__log__ = logging.getLogger(__name__)


def run_parameter(path, part):
    sys.path.append(str(path))

    with open(path / "input") as f:
        data = f.read().strip()
    data = aoc.lib.parse.parse_blocks(data)
    solution = importlib.import_module("solution")
    data = solution.Solution.prepare(data)

    func = getattr(solution.Solution, f"part_{part:02}")
    return (func, data)


def run(path, part):
    func, data = run_parameter(path, part)
    return func(data)


def cmd_run(args):
    func, data = run_parameter(args.current, args.part.value)
    func = aoc.lib.profile.profile(func)
    result = func(data)
    s = io.StringIO()
    ps = pstats.Stats(func.__profile__, stream=s).strip_dirs().sort_stats("cumulative")
    ps.print_stats(30)
    print(s.getvalue())
    print("The Answer is %s", repr(result))


def cmd_answer(args):
    answer = args.answer or run(args.current, args.part.value)
    __log__.info(
        "Send answer %s to mission (Year %d, Day %d, Part %d)",
        repr(answer),
        args.year,
        args.day,
        args.part.value,
    )
    result = args.api.answer(args.year, args.day, args.part.value, answer)
    if result.startswith("That's the right answer!"):
        termcolor.cprint(result.split("! ")[0] + "!", "green")
    elif result.startswith(
        "You don't seem to be solving the right level. Did you already complete it?"
    ):
        termcolor.cprint(result.split("? ")[0] + "?", "yellow")
    else:
        if result.startswith("That's not the right answer."):
            termcolor.cprint(result.split(". ")[0] + ".", "red")
            until = datetime.datetime.now() + datetime.timedelta(seconds=60)
        elif result.startswith("You gave an answer too recently;"):
            # you have to wait after submitting an answer before trying again. You have 29s left to wait."):
            termcolor.cprint(result.split("; ")[0] + ";", "red")
            delay = result.split(". ")[1] + "."
            m = re.match("You have (?P<delay>.*) left to wait.", delay)
            if m:
                until = dateparser.parse("in " + m.group("delay"))
        if isinstance(until, datetime.datetime):
            until = "Until %s" % until.isoformat(timespec="seconds")
        print(
            "You have to wait after submitting an answer before trying again. (%s)"
            % until
        )


class Level(enum.IntEnum):
    ONE = 1
    TWO = 2


def add_part_argument(parser):
    parser.add_argument("part", type=Level, action=aoc.misc.arguments.EnumAction)


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("run")
    parser.set_defaults(func=cmd_run)

    add_part_argument(parser)

    parser = parent_parser.add_parser("answer")
    parser.set_defaults(func=cmd_answer)

    add_part_argument(parser)

    parser.add_argument(
        "answer",
        nargs="?",
        type=str,
    )
