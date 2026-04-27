"""Display-p3 color class."""
from __future__ import annotations
from .srgb_linear import sRGBLinear
from .srgb import inverse_eotf_srgb, eotf_srgb
from ..types import Vector


class DisplayP3(sRGBLinear):
    """Display-p3 class."""

    BASE = "display-p3-linear"
    NAME = "display-p3"

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Display P3."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Display P3."""
        pass
