import argparse
import contextlib
import datetime
import pathlib
import re

import git

from aoc import command

import logging


__log__ = logging.getLogger(__name__)


def type_directory(string):
    result = pathlib.Path(string)
    if not result.is_dir():
        raise argparse.ArgumentError(f"{string:r}: no such directory")
    return result


def setup_parser(parser):
    repo = None
    with contextlib.suppress(git.InvalidGitRepositoryError):
        repo = git.Repo(".", search_parent_directories=True)
        repo = pathlib.Path(repo.working_tree_dir)
    parser.add_argument(
        "-b",
        "--base",
        default=repo,
        type=str,
        help="base dir of your solutions",
        metavar="BASE",
        required=not repo,
    )

    cookie = None
    if repo:
        with contextlib.suppress(
            FileNotFoundError, PermissionError, IsADirectoryError
        ), open(repo / ".session") as f:
            cookie = f.read().strip()

    parser.add_argument(
        "-c",
        "--cookie",
        default=cookie,
        type=str,
        help="session cookie for adventofcode.com",
        metavar="COOKIE",
        required=not cookie,
    )

    now = datetime.datetime.now()
    year = now.year
    day = now.day
    cwd = pathlib.Path.cwd()
    p = re.compile(r"/y(?P<year>\d+)(/d(?P<day>\d{2})(/|$))?")
    m = p.search(str(cwd))
    if m:
        year = int(m.group("year") or year)
        day = int(m.group("day") or day)
    parser.add_argument(
        "-y",
        "--year",
        default=year,
        type=int,
        choices=range(2015, now.year + 1),
        help=f"year of AoC event (2015..{now.year})",
        metavar="YEAR",
    )

    parser.add_argument(
        "-d",
        "--day",
        default=day,
        type=int,
        choices=range(1, 26),
        help="day of AoC event (1..25)",
        metavar="DAY",
    )

    subparsers = parser.add_subparsers(dest="cmd", required=True)

    command.init.setup_parser(subparsers)
    command.run.setup_parser(subparsers)
    command.stars.setup_parser(subparsers)
    command.test.setup_parser(subparsers)
