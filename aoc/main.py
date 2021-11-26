"""Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

You might be tempted to import things from __main__ later, but that will cause
problems: the code will get executed twice:

  - When you run `python -m aoc` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``aoc.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``aoc.__main__`` in ``sys.modules``.

Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import logging

from typing import List, Optional

import aoc

from . import arguments


logger = logging.getLogger(__name__)


def set_loglevel(args):
    pass


def main(args: Optional[List[str]] = None) -> int:
    """Console script for aoc.

    Args:
        args: Commandline arguments to parse

    Returns:
        exit code
    """
    parser = argparse.ArgumentParser(description=aoc.__summary__)
    parser.add_argument(
        "--version",
        action="version",
        version=f"{ aoc.__name__ } { aoc.__version__ }",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase output verbosity",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="count",
        default=0,
        help="decrease output verbosity",
    )

    arguments.setup_parser(parser)

    parsed = parser.parse_args(args=args)

    parsed.current = parsed.base / f"{parsed.year}" / f"{parsed.day:02d}"
    parsed.api = aoc.API(parsed.cookie)

    set_loglevel(parsed)

    logger.debug(f"Arguments: {parsed}")
    return parsed.func(parsed)
