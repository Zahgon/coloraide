"""
XYB color space.

https://ds.jpeg.org/whitepapers/jpeg-xl-whitepaper.pdf
"""
from __future__ import annotations
from .. import algebra as alg
from .lab import Lab
from ..types import Vector
from ..cat import WHITES
from ..channels import Channel, FLG_MIRROR_PERCENT

BIAS = 0.00379307325527544933
try:
    BIAS_CBRT = alg.nth_root(BIAS, 3)
except (NotImplementedError, TypeError, AttributeError):
    BIAS_CBRT = 0.0

LRGB_TO_LMS = [
    [0.3, 0.622, 0.078],
    [0.23, 0.692, 0.078],
    [0.24342268924547819, 0.20476744424496821, 0.55180986650955360]
]

LMS_TO_LRGB = [
    [11.031566904639865, -9.866943908131564, -0.16462299650829934],
    [-3.254147381074425, 4.4187703775827245, -0.16462299650829929],
    [-3.6588512867136815, 2.712923045936092, 1.945928240777589]
]

XYB_LMS_TO_XYB = [
    [0.5, -0.5, 0.0],
    [0.5, 0.5, 0.0],
    [0.0, 0.0, 1.0]
]

XYB_TO_XYB_LMS = [
    [1.0, 1.0, 0.0],
    [-1.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]


def rgb_to_xyb(rgb: Vector) -> Vector:
    """Linear sRGB to XYB."""
    pass


def xyb_to_rgb(xyb: Vector) -> Vector:
    """XYB to linear sRGB."""
    pass


class XYB(Lab):
    """XYB color class."""

    BASE = 'srgb-linear'
    NAME = "xyb"
    SERIALIZE = ("--xyb",)
    WHITE = WHITES['2deg']['D65']
    CHANNELS = (
        Channel("x", -0.05, 0.05, flags=FLG_MIRROR_PERCENT),
        Channel("y", 0.0, 0.845),
        Channel("b", -0.45, 0.45, flags=FLG_MIRROR_PERCENT)
    )

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def names(self) -> tuple[Channel, ...]:
        """Return Lab-ish names in the order L a b."""
        pass

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYB from base."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From base to XYB."""
        pass
