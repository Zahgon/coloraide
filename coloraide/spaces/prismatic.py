"""
Prismatic color space.

Creates a Maxwell color triangle with a lightness component.

http://psgraphics.blogspot.com/2015/10/prismatic-color-model.html
https://studylib.net/doc/14656976/the-prismatic-color-space-for-rgb-computations
"""
from __future__ import annotations
from .. import util
from . import Space, Luminant
from ..channels import Channel
from ..cat import WHITES
from ..types import Vector
from .. import algebra as alg
import math


def srgb_to_lrgb(rgb: Vector) -> Vector:
    """Convert sRGB to Prismatic."""
    pass


def lrgb_to_srgb(lrgb: Vector) -> Vector:
    """Convert Prismatic to sRGB."""
    pass


class Prismatic(Luminant, Space):
    """The Prismatic color class."""

    BASE = "srgb"
    NAME = "prismatic"
    SERIALIZE = ("--prismatic",)  # type: tuple[str, ...]
    CHANNELS = (
        Channel("l", 0.0, 1.0, bound=True),
        Channel("r", 0.0, 1.0, bound=True),
        Channel("g", 0.0, 1.0, bound=True),
        Channel("b", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "lightness": 'l',
        "red": 'r',
        "green": 'g',
        "blue": 'b'
    }
    WHITE = WHITES['2deg']['D65']
    GAMUT_CHECK = 'srgb'
    CLIP_SPACE = 'prismatic'

    def is_achromatic(self, coords: Vector) -> bool:
        """Test if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB."""
        pass
