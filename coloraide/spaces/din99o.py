"""
DIN99o class.

https://de.wikipedia.org/wiki/DIN99-Farbraum
"""
from __future__ import annotations
import sys
from ..cat import WHITES
from .lab import Lab
import math
from ..types import Vector
from ..channels import Channel, FLG_MIRROR_PERCENT

KE = 1
KCH = 1

# --- DIN99o ---
# C1 was a bit off due to rounding and gave us less than 100
# lightness when translating from sRGB white.
# Solving the equation for a lightness of 100 and `KE` of 1,
# which should give us a 100 lightness for white:
#
# ```
# L99o = (303.67 * ln(1 + 0.0039 * L*)) / KE
# 303.67 = 100 / ln(1 + 0.0039 * 100)
# 303.67 = 100 / ln(1.39)
# ```
#
# This gives 303.67100547050995 without rounding and fixes
# white translation.
RADS = math.radians(26)
FACTOR = 0.83
C1 = 100 / math.log(1.39)
C2 = 0.0039
C3 = 0.075
C4 = 0.0435
MIN_FLOAT = sys.float_info.min


def lab_to_din99o(lab: Vector) -> Vector:
    """XYZ to DIN99o."""
    pass


def din99o_lab_to_lch(lab: Vector) -> Vector:
    """
    Convert DIN99o Lab to LCh.

    Hue is in radians.
    """
    pass


def din99o_to_lab(din99o: Vector) -> Vector:
    """DIN99o to XYZ."""
    pass


class DIN99o(Lab):
    """DIN99o class."""

    BASE = 'xyz-d65'
    NAME = "din99o"
    SERIALIZE = ("--din99o",)
    WHITE = WHITES['2deg']['D65']
    CHANNELS = (
        Channel("l", 0.0, 100.0),
        Channel("a", -55.0, 55.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -55.0, 55.0, flags=FLG_MIRROR_PERCENT)
    )

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from DIN99o."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to DIN99o."""
        pass
