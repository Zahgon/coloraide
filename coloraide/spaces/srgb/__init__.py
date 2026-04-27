"""sRGB color class."""
from __future__ import annotations
from ..srgb_linear import sRGBLinear
from ... import algebra as alg
from ...types import Vector
import math


def eotf_srgb(rgb: Vector) -> Vector:
    """
    Convert an array of sRGB values in the range 0.0 - 1.0 to linear light (un-corrected) form.

    https://en.wikipedia.org/wiki/SRGB
    """
    pass


def inverse_eotf_srgb(rgb: Vector) -> Vector:
    """
    Convert an array of linear-light sRGB values in the range 0.0-1.0 to gamma corrected form.

    https://en.wikipedia.org/wiki/SRGB
    """
    pass


class sRGB(sRGBLinear):
    """sRGB class."""

    BASE = "srgb-linear"
    NAME = "srgb"
    SERIALIZE = ("srgb",)

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB Linear to sRGB."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB Linear from sRGB."""
        pass
