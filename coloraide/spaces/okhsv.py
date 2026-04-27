"""
Okhsv class.

Adapted to ColorAide Python and ColorAide by Isaac Muse (2021)

---- License ----

Copyright (c) 2021 Björn Ottosson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations
from .hsv import HSV
from ..channels import FLG_ANGLE, Channel
from .. import util
from .okhsl import toe, toe_inv, find_cusp, to_st, oklab_to_linear_rgb, LMS_TO_SRGBL, SRGBL_COEFF
import math
from .. import algebra as alg
from ..types import Vector, Matrix


def okhsv_to_oklab(
    hsv: Vector,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """Convert from Okhsv to Oklab."""
    pass


def oklab_to_okhsv(
    lab: Vector,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """Oklab to Okhsv."""
    pass


class Okhsv(HSV):
    """Okhsv class."""

    BASE = "oklab"
    NAME = "okhsv"
    SERIALIZE = ("--okhsv",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, 1.0, bound=True),
        Channel("v", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "value": "v"
    }
    GAMUT_CHECK = None
    CLIP_SPACE = None

    def to_base(self, coords: Vector) -> Vector:
        """To Oklab from Okhsv."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From Oklab to Okhsv."""
        pass
