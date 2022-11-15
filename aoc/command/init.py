import inspect

import logging


__log__ = logging.getLogger(__name__)


def cmd_init(args):
    args.current.mkdir(parents=True, exist_ok=True)

    init = args.current / "__init__.py"
    if not init.is_file():
        with open(init, "w") as f:
            pass

    solution = args.current / "solution.py"
    if not solution.is_file():
        with open(solution, "w") as f:
            import aoc.template.solution

            f.write(inspect.getsource(aoc.template.solution))

    test = args.current / "test.py"
    if not test.is_file():
        with open(test, "w") as f:
            import aoc.template.test

            f.write(inspect.getsource(aoc.template.test))

    readme = args.current / "README.md"
    if not readme.is_file():
        with open(readme, "w") as f:
            f.write(args.api.mission(args.year, args.day))

    data = args.current / "input"
    if not data.is_file():
        with open(data, "w") as f:
            f.write(args.api.data(args.year, args.day))

    answers = args.current / "answers"
    if not answers.is_file():
        with open(answers, "w") as f:
            f.write("\n".join(args.api.answers(args.year, args.day)) + "\n")


def cmd_update(args):
    args.current.mkdir(parents=True, exist_ok=True)

    readme = args.current / "README.md"
    with open(readme, "w") as f:
        f.write(args.api.mission(args.year, args.day))

    data = args.current / "input"
    if not data.is_file():
        with open(data, "w") as f:
            f.write(args.api.data(args.year, args.day))

    answers = args.current / "answers"
    with open(answers, "w") as f:
        f.write("\n".join(args.api.answers(args.year, args.day)) + "\n")


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("init")
    parser.set_defaults(func=cmd_init)
    parser = parent_parser.add_parser("update")
    parser.set_defaults(func=cmd_update)
