"""
Rec. 2100 PQ color class.

https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2100-2-201807-I!!PDF-E.pdf
"""
from __future__ import annotations
from ..cat import WHITES
from .srgb_linear import sRGBLinear
from ..types import Vector
from .. import util

YW = 203


class Rec2100PQ(sRGBLinear):
    """Rec. 2100 PQ class."""

    BASE = "rec2100-linear"
    NAME = "rec2100-pq"
    SERIALIZE = ('rec2100-pq', '--rec2100-pq',)
    WHITE = WHITES['2deg']['D65']
    DYNAMIC_RANGE = 'hdr'

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To base from Rec. 2100 PQ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From base to Rec. 2100 PQ."""
        pass
