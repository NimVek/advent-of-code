import contextlib

import git
import termcolor

import logging


__log__ = logging.getLogger(__name__)


def cmd_stars(args):
    events = args.api.User().stars(verbose=True)
    __log__.debug(events)

    args.api.update_readme(args.base, events)

    repo = None
    with contextlib.suppress(git.InvalidGitRepositoryError):
        repo = git.Repo(args.base)

    for year, days in sorted(events.items()):
        print(year, end=" ")
        if isinstance(days, int):
            print(f"{days:2}/50")
        else:
            for day in range(1, 26):
                stars = days.get(day, 3)
                colour = ["red", "yellow", "green", "grey"][stars]
                solution = args.base / f"y{year}" / f"d{day:02}" / "solution.py"
                attributes = (
                    [] if solution.is_file() or stars in [0, 3] else ["reverse"]
                )
                if repo:
                    with contextlib.suppress(KeyError):
                        repo.commit().tree[f"y{year}/d{day:02}/solution.py"]
                        attributes.append("bold")
                termcolor.cprint(f"{day:2}", colour, attrs=attributes, end=" ")
            print()


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("stars")
    parser.set_defaults(func=cmd_stars)
