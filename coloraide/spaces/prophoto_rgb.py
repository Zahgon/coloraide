"""Pro Photo RGB color class."""
from __future__ import annotations
from ..cat import WHITES
from .srgb_linear import sRGBLinear
from .. import algebra as alg
from ..types import Vector

ET = 1 / 512
ET2 = 16 / 512


def lin_prophoto(rgb: Vector) -> Vector:
    """
    Convert an array of prophoto-rgb values in the range 0.0 - 1.0 to linear light (un-corrected) form.

    Transfer curve is gamma 1.8 with a small linear portion.

    https://en.wikipedia.org/wiki/ProPhoto_RGB_color_space
    """
    pass


def gam_prophoto(rgb: Vector) -> Vector:
    """
    Convert an array of linear-light prophoto-rgb  in the range 0.0-1.0 to gamma corrected form.

    Transfer curve is gamma 1.8 with a small linear portion.

    https://en.wikipedia.org/wiki/ProPhoto_RGB_color_space
    """
    pass


class ProPhotoRGB(sRGBLinear):
    """Pro Photo RGB class."""

    BASE = "prophoto-rgb-linear"
    NAME = "prophoto-rgb"
    WHITE = WHITES['2deg']['D50']

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Pro Photo RGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Pro Photo RGB."""
        pass
