import logging
import re

from aoc.misc import color


logger = logging.getLogger(__name__)


def cmd_stars(args):
    stars = args.api.stars()
    logger.debug(stars)
    readme = args.base / "README.md"
    with open(readme) as f:
        content = f.read()
    for year, count in stars.items():
        colour = color.color_scale(count, (0, 50)) if count else color.LIGHTGREY
        content = re.sub(
            rf"\(https:\/\/img\.shields\.io\/badge\/{year}-★_[^)]*\)",
            f"(https://img.shields.io/badge/{year}-★_{count}-{colour.html})",
            content,
        )
    with open(readme, "w") as f:
        f.write(content)


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("stars")
    parser.set_defaults(func=cmd_stars)
