"""
Rec. 2020 color space (scene referred).

Uses the default OETF specified in the ITU-R BT2020 spec.
https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2020-2-201510-I!!PDF-E.pdf
"""
from __future__ import annotations
import math
from .rec2020 import Rec2020
from .. import algebra as alg
from ..types import Vector

ALPHA = 1.09929682680944
BETA = 0.018053968510807
BETA45 = BETA * 4.5
ALPHAM1 = ALPHA - 1


def inverse_oetf_bt2020(rgb: Vector) -> Vector:
    """Convert an array of rec-2020 RGB values in the range 0.0 - 1.0 to linear light (un-corrected) form."""
    pass


def oetf_bt2020(rgb: Vector) -> Vector:
    """Convert an array of linear-light rec-2020 RGB  in the range 0.0-1.0 to gamma corrected form."""
    pass


class Rec2020OETF(Rec2020):
    """Rec 2020 class using OETF gamma correction."""

    NAME = "rec2020-oetf"
    SERIALIZE = ("--rec2020-oetf",)

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Rec. 2020."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Rec. 2020."""
        pass
