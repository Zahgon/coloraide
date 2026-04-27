"""
ACEScc color space.

https://www.oscars.org/science-technology/aces/aces-documentation
"""
from __future__ import annotations
import math
from ..channels import Channel
from .srgb_linear import sRGBLinear
from ..cat import WHITES
from ..types import Vector

CC_MIN = (math.log2(2 ** -16) + 9.72) / 17.52
CC_MAX = (math.log2(65504) + 9.72) / 17.52


def acescc_to_acescg(acescc: Vector) -> Vector:
    """Convert ACEScc to XYZ."""
    pass


def acescg_to_acescc(acescg: Vector) -> Vector:
    """Convert XYZ to ACEScc."""
    pass


class ACEScc(sRGBLinear):
    """The ACEScc color class."""

    BASE = "acescg"
    NAME = "acescc"
    SERIALIZE = ("--acescc",)  # type: tuple[str, ...]
    WHITE = WHITES['2deg']['ACES-D60']
    CHANNELS = (
        Channel("r", CC_MIN, CC_MAX, bound=True, nans=CC_MIN),
        Channel("g", CC_MIN, CC_MAX, bound=True, nans=CC_MIN),
        Channel("b", CC_MIN, CC_MAX, bound=True, nans=CC_MIN)
    )
    DYNAMIC_RANGE = 'hdr'

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ."""
        pass
