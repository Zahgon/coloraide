"""
Uncalibrated, naive CMYK color space.

https://www.w3.org/TR/css-color-5/#cmyk-rgb
"""
from __future__ import annotations
from .. import util
from . import Space
from ..channels import Channel
from ..cat import WHITES
from ..types import Vector
from .. import algebra as alg
import math


def srgb_to_cmyk(cmy: Vector) -> Vector:
    """Convert sRGB to CMYK."""
    pass


def cmyk_to_srgb(cmyk: Vector) -> Vector:
    """Convert CMYK to sRGB."""
    pass


class CMYK(Space):
    """The CMYK color class."""

    BASE = "cmy"
    NAME = "cmyk"
    SERIALIZE = ("--cmyk",)  # type: tuple[str, ...]
    CHANNELS = (
        Channel("c", 0.0, 1.0, bound=True),
        Channel("m", 0.0, 1.0, bound=True),
        Channel("y", 0.0, 1.0, bound=True),
        Channel("k", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "cyan": 'c',
        "magenta": 'm',
        "yellow": 'y',
        "black": 'k'
    }
    WHITE = WHITES['2deg']['D65']
    SUBTRACTIVE = True
    GAMUT_CHECK = 'cmy'
    CLIP_SPACE = 'cmyk'

    def is_achromatic(self, coords: Vector) -> bool:
        """Test if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB."""
        pass
