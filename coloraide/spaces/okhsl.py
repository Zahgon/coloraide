"""
Okhsl class.

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
from .hsl import HSL
from ..channels import Channel, FLG_ANGLE
from .. import util
import math
import sys
from .. import algebra as alg
from ..types import Vector, Matrix
from . oklab import OKLAB_TO_LMS3

SRGBL_TO_LMS = [
    [0.4122214694707629, 0.5363325372617349, 0.051445993267502196],
    [0.2119034958178251, 0.6806995506452345, 0.10739695353694051],
    [0.08830245919005637, 0.2817188391361215, 0.6299787016738223]
]

LMS_TO_SRGBL = [
    [4.076741636075959, -3.307711539258062, 0.2309699031821041],
    [-1.2684379732850313, 2.6097573492876878, -0.3413193760026569],
    [-0.004196076138675526, -0.703418617935936, 1.7076146940746113]
]

SRGBL_COEFF = [
    # Red
    [
        # Limit
        [-1.8817031, -0.80936501],
        # `Kn` coefficients
        [1.19086277, 1.76576728, 0.59662641, 0.75515197, 0.56771245]
    ],
    # Green
    [
        # Limit
        [1.8144408, -1.19445267],
        # `Kn` coefficients
        [0.73956515, -0.45954404, 0.08285427, 0.12541073, -0.14503204]
    ],
    # Blue
    [
        # Limit
        [0.13110758, 1.81333971],
        # `Kn` coefficients
        [1.35733652, -0.00915799, -1.1513021, -0.50559606, 0.00692167]
    ]
]  # type: list[Matrix]

FLT_MAX = sys.float_info.max

K_1 = 0.206
K_2 = 0.03
K_3 = (1.0 + K_1) / (1.0 + K_2)


def toe(x: float, k1: float = K_1, k2: float = K_2, k3: float = K_3) -> float:
    """Toe function for L_r."""
    pass


def toe_inv(x: float, k1: float = K_1, k2: float = K_2, k3: float = K_3) -> float:
    """Inverse toe function for L_r."""
    pass


def to_st(cusp: Vector) -> Vector:
    """To ST."""
    pass


def get_st_mid(a: float, b: float) -> Vector:
    """
    Returns a smooth approximation of the location of the cusp.

    This polynomial was created by an optimization process.
    It has been designed so that S_mid < S_max and T_mid < T_max.
    """
    pass


def oklab_to_linear_rgb(lab: Vector, lms_to_rgb: Matrix) -> Vector:
    """
    Convert from Oklab to linear RGB.

    Can be any gamut as long as `lms_to_rgb` is a matrix
    that transform the LMS values to the linear RGB space.
    """
    pass


def find_cusp(
    a: float,
    b: float,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """
    Finds L_cusp and C_cusp for a given hue.

    `a` and `b` must be normalized so `a^2 + b^2 == 1`.
    """
    pass


def find_gamut_intersection(
    a: float,
    b: float,
    l1: float,
    c1: float,
    l0: float,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix],
    cusp: Vector | None = None,
) -> float:
    """
    Finds intersection of the line.

    Defined by the following:

    ```
    L = L0 * (1 - t) + t * L1
    C = t * C1
    ```

    `a` and `b` must be normalized so `a^2 + b^2 == 1`.
    """
    pass


def get_cs(
    lab: Vector,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """Get Cs."""
    pass


def compute_max_saturation(
    a: float,
    b: float,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> float:
    """
    Finds the maximum saturation possible for a given hue that fits in RGB.

    Saturation here is defined as `S = C/L`.
    `a` and `b` must be normalized so `a^2 + b^2 == 1`.
    """
    pass


def okhsl_to_oklab(
    hsl: Vector,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """Convert Okhsl to Oklab."""
    pass


def oklab_to_okhsl(
    lab: Vector,
    lms_to_rgb: Matrix,
    ok_coeff: list[Matrix]
) -> Vector:
    """Oklab to Okhsl."""
    pass


class Okhsl(HSL):
    """HSL class."""

    BASE = "oklab"
    NAME = "okhsl"
    SERIALIZE = ("--okhsl",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, 1.0, bound=True),
        Channel("l", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "lightness": "l"
    }
    GAMUT_CHECK = None
    CLIP_SPACE = None

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To Oklab from Okhsl."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From Oklab to Okhsl."""
        pass
