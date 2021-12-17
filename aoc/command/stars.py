import colorsys
import logging
import re


logger = logging.getLogger(__name__)


def cmd_stars(args):
    stars = args.api.stars()
    logger.debug(stars)
    readme = args.base / "README.md"
    with open(readme) as f:
        content = f.read()
    for year, stars in stars.items():
        color = colorsys.hsv_to_rgb(stars / 50 / 3, 1, 1)
        color = "".join([f"{int(i * 255):02x}" for i in color])
        content = re.sub(
            fr"\(https:\/\/img\.shields\.io\/badge\/{year}-★_[^)]*\)",
            f"(https://img.shields.io/badge/{year}-★_{stars}-{color})",
            content,
        )
    with open(readme, "w") as f:
        f.write(content)


def setup_parser(parent_parser):
    parser = parent_parser.add_parser("stars")
    parser.set_defaults(func=cmd_stars)
