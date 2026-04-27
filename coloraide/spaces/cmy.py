"""Uncalibrated, naive CMY color space."""
from __future__ import annotations
from .. import util
from . import Prism, Space
from .srgb import sRGB
from ..channels import Channel
from ..cat import WHITES
from ..types import Vector
from .. import algebra as alg
import math


def srgb_to_cmy(rgb: Vector) -> Vector:
    """Convert sRGB to CMY."""
    pass


def cmy_to_srgb(cmy: Vector) -> Vector:
    """Convert CMY to sRGB."""
    pass


class CMY(Prism, Space):
    """The CMY color class."""

    BASE = "srgb"
    NAME = "cmy"
    SERIALIZE = ("--cmy",)  # type: tuple[str, ...]
    CHANNELS = (
        Channel("c", 0.0, 1.0, bound=True),
        Channel("m", 0.0, 1.0, bound=True),
        Channel("y", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "cyan": 'c',
        "magenta": 'm',
        "yellow": 'y'
    }
    WHITE = WHITES['2deg']['D65']
    SUBTRACTIVE = True

    def linear(self) -> str:
        """Linear."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Test if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB."""
        pass
