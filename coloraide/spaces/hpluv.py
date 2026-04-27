"""
HPLuv color space.

Adapted to Python and ColorAide by Isaac Muse (2021)

--- HSLuv Conversion Algorithm ---
Copyright (c) 2012-2021 Alexei Boronine
Copyright (c) 2016 Florian Dormont

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
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
from .hsl import HSL
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from .lab import EPSILON, KAPPA
from .srgb_linear import XYZ_TO_RGB
import math
from .. import algebra as alg
from .. import util
from ..types import Vector


def distance_line_from_origin(line: tuple[float, float]) -> float:
    """Distance line from origin."""
    pass


def get_bounds(l: float) -> list[tuple[float, float]]:
    """Get bounds."""
    pass


def max_safe_chroma_for_l(l: float) -> float:
    """Get safe max chroma for lightness."""
    pass


def hpluv_to_luv(hpluv: Vector) -> Vector:
    """Convert HPLuv to LCh."""
    pass


def luv_to_hpluv(luv: Vector) -> Vector:
    """Convert LCh to HPLuv."""
    pass


class HPLuv(HSL):
    """HPLuv class."""

    BASE = 'luv'
    NAME = "hpluv"
    SERIALIZE = ("--hpluv",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("p", 0.0, 100.0, bound=True),
        Channel("l", 0.0, 100.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "perpendiculars": "p",
        "lightness": "l"
    }
    WHITE = WHITES['2deg']['D65']
    GAMUT_CHECK = None

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def radial_name(self) -> str:
        """Radial name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To LChuv from HPLuv."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From LChuv to HPLuv."""
        pass
