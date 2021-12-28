import colorsys
import logging
import math

from dataclasses import dataclass


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Color:
    def __init__(
        self,
        rgb: tuple[int, int, int] = None,
        hsv: tuple[int, int, int] = None,
        html: str = None,
    ):
        if rgb is not None:
            super().__setattr__("rgb", rgb)
        elif rgb is None and hsv is not None:
            super().__setattr__("rgb", colorsys.hsv_to_rgb(*hsv))
        elif rgb is None and html is not None:
            html = [html[i : i + 2] for i in range(0, len(html), 2)]
            html = map(lambda x: int(x, 16) / 255, html)
            super().__setattr__("rgb", tuple(html))

    @property
    def hsv(self):
        return colorsys.rgb_to_hsv(*self.rgb)

    @property
    def html(self):
        return "".join([f"{int(i * 255):02x}" for i in self.rgb])


BRIGHTGREEN = Color(html="44cc11")
GREEN = Color(html="97ca00")
YELLOW = Color(html="dfb317")
YELLOWGREEN = Color(html="a4a61d")
ORANGE = Color(html="fe7d37")
RED = Color(html="e05d44")
BLUE = Color(html="007ec6")
GREY = Color(html="555555")
LIGHTGREY = Color(html="9f9f9f")


def interpolate_color(start: Color, end: Color, mark: float):
    start = start.hsv
    end = end.hsv
    result = [(a + (b - a) * mark) for a, b in zip(start, end)]
    result[0] = start[0] + (end[0] - start[0] - round(end[0] - start[0])) * mark
    return Color(hsv=result)


TRAFFIC_LIGHT = [RED, ORANGE, YELLOWGREEN, YELLOW, GREEN, BRIGHTGREEN]


def color_scale(value, range_, scale=None):
    if scale is None:
        scale = TRAFFIC_LIGHT
    idx = (value - range_[0]) * (len(scale) - 1) / (range_[1] - range_[0])
    color = scale[math.floor(idx) : math.ceil(idx) + 1]
    if len(color) == 1:
        return color[0]
    return interpolate_color(color[0], color[1], idx - math.floor(idx))
