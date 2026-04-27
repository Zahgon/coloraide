"""
The xyY color space.

https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space
"""
from __future__ import annotations
from . import Space, Prism, Luminant
from ..channels import Channel
from ..cat import WHITES
from .. import util
from ..types import Vector
from .. import algebra as alg
import math


class xyY(Luminant, Prism, Space):
    """The xyY class."""

    BASE = "xyz-d65"
    NAME = "xyy"
    SERIALIZE = ("--xyy",)
    CHANNELS = (
        Channel("x", 0.0, 1.0),
        Channel("y", 0.0, 1.0),
        Channel("Y", 0.0, 1.0)
    )
    WHITE = WHITES['2deg']['D65']

    def is_achromatic(self, coords: Vector) -> bool:
        """Test if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ."""
        pass

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass
