import re

import termcolor

from aoc.misc import color

import logging


__log__ = logging.getLogger(__name__)


def cmd_stars(args):
    events = args.api.stars(verbose=True)
    __log__.debug(events)
    readme = args.base / "README.md"
    with open(readme) as f:
        content = f.read()
    for year, days in events.items():
        stars = days if isinstance(days, int) else sum(days.values())
        colour = color.color_scale(stars, (0, 50)) if stars else color.LIGHTGREY
        content = re.sub(
            rf"\(https:\/\/img\.shields\.io\/badge\/{year}-★_[^)]*\)",
            f"(https://img.shields.io/badge/{year}-★_{stars}-{colour.html})",
            content,
        )
    with open(readme, "w") as f:
        f.write(content)
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
                termcolor.cprint(f"{day:2}", colour, attrs=attributes, end=" ")
            print()


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("stars")
    parser.set_defaults(func=cmd_stars)
