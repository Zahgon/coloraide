"""
RYB color space.

Gosset and Chen
http://bahamas10.github.io/ryb/assets/ryb.pdf
"""
from __future__ import annotations
import math
from .. import util
from . import Prism, Space
from .. import algebra as alg
from ..channels import Channel
from ..cat import WHITES
from ..types import Vector, Matrix

# In terms of RGB
GOSSET_CHEN_CUBE = [
    [1.0, 1.0, 1.0],      # White (c000)
    [1.0, 0.0, 0.0],      # Red (c100)
    [1.0, 1.0, 0.0],      # Yellow (C010)
    [1.0, 0.5, 0.0],      # Orange (c110)
    [0.163, 0.373, 0.6],  # Blue (c001)
    [0.5, 0.0, 0.5],      # Violet (c101)
    [0.0, 0.66, 0.2],     # Green (c011)
    [0.2, 0.094, 0.0]     # Black (c111)
]  # type: Matrix


def cubic_poly(t: float, a: float, b: float, c: float, d: float) -> float:
    """Cubic polynomial."""
    pass


def cubic_poly_dt(t: float, a: float, b: float, c: float) -> float:
    """Derivative of cubic polynomial."""
    pass


def solve_cubic_poly(a: float, b: float, c: float, d: float) -> float:
    """
    Solve curve to find a `t` that satisfies our desired `x`.

    Using `alg.solve_poly` is actually faster and more accurate as it is an
    analytical approach. Since we are using Newton's method for the inverse
    trilinear interpolation, which is only accurate to around 1e-6 in our case,
    applying a very accurate cubic solver to a not so accurate inverse interpolation
    can actually give us an even more inaccurate result. This is evident in our use
    case around RYB [1, 1, 0] which can drop to around 1e-3 accuracy.

    Using an approach where we can better control accuracy and limit it to a similar accuracy
    of 1e-6 actually helps us maintain a minimum of 1e-6 accuracy through the sRGB
    gamut giving more consistent results within the trilinear cube.
    """
    pass


def srgb_to_ryb(rgb: Vector, cube_t: Matrix, cube: Matrix, biased: bool) -> Vector:
    """Convert RYB to sRGB."""
    pass


def ryb_to_srgb(ryb: Vector, cube_t: Matrix, biased: bool) -> Vector:
    """Convert RYB to sRGB."""
    pass


class RYB(Prism, Space):
    """
    The RYB color space based on the paper by Gosset and Chen.

    The easing function for biasing colors towards the vertices is not handled in this color space.
    """

    NAME = "ryb"
    BASE = "srgb"
    SERIALIZE = ("--ryb",)
    CHANNELS = (
        Channel("r", 0.0, 1.0, bound=True),
        Channel("y", 0.0, 1.0, bound=True),
        Channel("b", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "red": 'r',
        "yellow": 'y',
        "blue": 'b'
    }
    WHITE = WHITES['2deg']['D65']
    RYB_CUBE = GOSSET_CHEN_CUBE
    try:
        RYB_CUBE_T = alg.transpose(RYB_CUBE)
    except (NotImplementedError, TypeError, AttributeError):
        RYB_CUBE_T = None  # type: ignore[assignment]
    BIASED = False
    SUBTRACTIVE = True

    def is_achromatic(self, coords: Vector) -> bool:
        """
        Test if color is achromatic.

        Achromatic colors in the traditional sense is just brown in RYB,
        so convert to RGB where it is easier to determine an actual achromatic color.
        """
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB."""
        pass


class RYBBiased(RYB):
    """
    Gosset and Chen RYB with biasing towards the vertices.

    This mimics exactly what was done in the paper.
    """

    NAME = "ryb-biased"
    SERIALIZE = ("--ryb-biased",)
    BIASED = True
