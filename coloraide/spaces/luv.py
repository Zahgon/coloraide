"""
Luv class.

https://en.wikipedia.org/wiki/CIELuv
"""
from __future__ import annotations
from ..cat import WHITES
from ..channels import Channel, FLG_MIRROR_PERCENT
from .lab import KAPPA, EPSILON, KE, Lab
from .. import util
from .. import algebra as alg
from ..types import Vector


def xyz_to_luv(xyz: Vector, white: tuple[float, float]) -> Vector:
    """XYZ to Luv."""
    pass


def luv_to_xyz(luv: Vector, white: tuple[float, float]) -> Vector:
    """Luv to XYZ."""
    pass


class Luv(Lab):
    """Luv class."""

    BASE = "xyz-d65"
    NAME = "luv"
    SERIALIZE = ("--luv",)
    CHANNELS = (
        Channel("l", 0.0, 100.0),
        Channel("u", -215.0, 215.0, flags=FLG_MIRROR_PERCENT),
        Channel("v", -215.0, 215.0, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "lightness": "l"
    }
    WHITE = WHITES['2deg']['D65']

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ D50 from Luv."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ D50 to Luv."""
        pass
