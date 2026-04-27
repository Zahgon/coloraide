"""
Lab class.

https://ia802802.us.archive.org/23/items/gov.law.cie.15.2004/cie.15.2004.pdf
http://www.brucelindbloom.com/Eqn_Lab_to_XYZ.html
"""
from __future__ import annotations
from .. import Space, Labish
from ...cat import WHITES
from ...channels import Channel, FLG_MIRROR_PERCENT
from ... import util
from ... import algebra as alg
from ...types import VectorLike, Vector
from typing import Any

EPSILON = 216 / 24389  # `6^3 / 29^3`
EPSILON3 = 6 / 29  # Cube root of EPSILON
KAPPA = 24389 / 27
KE = 8  # KAPPA * EPSILON = 8


def y_to_lstar(y: float) -> float:
    """Convert XYZ Y to Lab L*."""
    pass


def lstar_to_y(lstar: float) -> float:
    """Convert Lab L* to XYZ Y."""
    pass


def lab_to_xyz(lab: Vector, white: VectorLike) -> Vector:
    """Convert CIE Lab to XYZ using the reference white."""
    pass


def xyz_to_lab(xyz: Vector, white: VectorLike) -> Vector:
    """Convert XYZ to CIE Lab using the reference white."""
    pass


class Lab(Labish, Space):
    """Lab class."""

    CHANNELS = (
        Channel("l", 0.0, 1.0),
        Channel("a", -1.0, 1.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -1.0, 1.0, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "lightness": "l"
    }

    def __init__(self, **kwargs: Any):
        """Initialize."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ D50 from Lab."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ D50 to Lab."""
        pass


class CIELab(Lab):
    """CIE Lab D50."""

    BASE = "xyz-d50"
    NAME = "lab"
    SERIALIZE = ("--lab",)
    CHANNELS = (
        Channel("l", 0.0, 100.0),
        Channel("a", -125.0, 125.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -125.0, 125.0, flags=FLG_MIRROR_PERCENT)
    )
    WHITE = WHITES['2deg']['D50']
