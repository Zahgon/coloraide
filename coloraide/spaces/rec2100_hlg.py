"""
Rec 2100 HLG color class.

https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2100-2-201807-I!!PDF-E.pdf

https://www.itu.int/dms_pub/itu-r/opb/rep/R-REP-BT.2390-10-2021-PDF-E.pdf (page 25)

> Report ITU-R BT.2408 indicates that, for HLG HDR, diffuse white should be set at a signal level of
> 75%. This can be configured by making the output from an 18% grey card correspond to a signal
> level of 38%, rather than the 42.5% stated above.

https://lists.w3.org/Archives/Public/public-colorweb/2021Sep/0008.html

Suggests the scale of 0.26496256042100724 to satisfy the above requirement.

"""
from __future__ import annotations
from ..cat import WHITES
from .srgb_linear import sRGBLinear
from .. import algebra as alg
from ..types import Vector
import math

# Sets 18% grey card to ~38% (37.7...) in order to set diffused white to 75%.
SCALE = 0.26496256042100724


class Environment:
    """Class to calculate and contain any required environmental data."""

    def __init__(
        self,
        *,
        lw: float,
        lb: float,
        scale: float
    ):
        """Initialize environmental data."""
        pass


def hlg_gamma(lw: float = 1000.0) -> float:
    """
    Return the reference HLG system gamma.

    Ranges should be `lw >= 1000 cd / m^2`.
    """
    pass


def hlg_black_level_lift(lw: float = 0.0, lb: float = 1000.0) -> float:
    """
    Return beta (the black level lift) using the nominal peak level luminance and display luminance for black.

    Ranges should be `lw >= 1000 cd / m^2` and `lb <= 0.005 cd / m^2`.
    """
    pass


def oetf_hlg(values: Vector, env: Environment) -> Vector:
    """HLG OETF."""
    pass


def inverse_oetf_hlg(values: Vector, env: Environment) -> Vector:
    """HLG inverse OETF."""
    pass


class Rec2100HLG(sRGBLinear):
    """Rec. 2100 HLG class."""

    BASE = "rec2100-linear"
    NAME = "rec2100-hlg"
    SERIALIZE = ('rec2100-hlg', '--rec2100-hlg',)
    WHITE = WHITES['2deg']['D65']
    DYNAMIC_RANGE = 'hdr'
    ENV = Environment(
        lw=1000,
        lb=0,
        scale=SCALE
    )

    def linear(self) -> str:
        """Return linear version of the RGB (if available)."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To base from Rec 2100 HLG."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From base to Rec. 2100 HLG."""
        pass
