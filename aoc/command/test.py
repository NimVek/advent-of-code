import errno

import pytest


def cmd_test(args):
    targets = None
    if args.all:
        targets = set()
        for i in args.base.glob("**/test_solution.py"):
            targets.add(i.parent.parent)
    else:
        target = args.current
        if target.is_dir():
            targets = [target]

    if not targets:
        return errno.ENOENT
    return pytest.main(["--verbose", "--no-header"] + [str(x) for x in targets])


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("test")
    parser.set_defaults(func=cmd_test)

    parser.add_argument("-a", "--all", action="store_true", help="select all solutions")
