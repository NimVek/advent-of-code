import importlib
import pprint
import sys


def cmd_run(args):
    sys.path.append(str(args.current))

    with open(args.current / "input", "r") as f:
        input = f.read().strip()
    solution = importlib.import_module(f"solution_{args.year}_{args.day:02d}")

    pprint.pprint(getattr(solution, args.part)(input))


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
