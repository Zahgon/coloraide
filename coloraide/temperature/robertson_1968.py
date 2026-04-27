"""
Calculate CCT with Robertson 1968 method.

Uses Robertson 1968 method.

- https://en.wikipedia.org/wiki/Correlated_color_temperature#Robertson's_method
- http://www.brucelindbloom.com/index.html?Math.html
"""
from __future__ import annotations
import math
from . import planck
from .. import algebra as alg
from .. import util
from .. import cat
from .. import cmfs
from . import CCT
from ..types import Vector, VectorLike
from typing import Any, TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

# Original 31 mired points 0 - 600
MIRED_ORIGINAL = tuple(range(0, 100, 10)) + tuple(range(100, 601, 25))
# Extended 16 mired points 625 - 1000
MIRED_EXTENDED = MIRED_ORIGINAL + tuple(range(625, 1001, 25))


class CCTEntry(NamedTuple):
    """CCT LUT entry."""

    mired: float
    u: float
    v: float
    slope: float
    slope_length: float
    du: float
    dv: float


class Robertson1968(CCT):
    """Delta E plugin class."""

    NAME = 'robertson-1968'
    CHROMATICITY = 'uv-1960'

    def __init__(
        self,
        cmfs: cmfs.CMFs = cmfs.CIE_1931_2DEG,
        white: VectorLike = cat.WHITES['2deg']['D65'],
        mired: VectorLike = MIRED_EXTENDED,
        sigfig: int = 5,
        planck_step: int = 1,
    ) -> None:
        """Initialize."""
        pass

    def generate_table(
        self,
        cmfs: cmfs.CMFs,
        white: VectorLike,
        mired: VectorLike,
        sigfig: int,
        planck_step: int,
    ) -> list[CCTEntry]:
        """
        Generate the necessary table for the Robertson1968 method.

        The below algorithm, coupled with the 1nm CMFs for the 1931 2 degree table, allows us to replicate the
        documented 31 points exactly.

        For each mired value we calculate two additional points, one on each side at a distance of 0.1.
        We use a very small distance so that we can approximate the slope. We calculate the distance between
        the targeted value and the two neighbors and then calculate the slope of the two small lines. Then we
        can calculate an interpolation factor and interpolate the slope for our target.

        We are able to calculate the uv pair for each mired point directly except for 0. 0 requires us to
        interpolate the values as it will cause a divide by zero in the Planckian locus. In this case, we
        assume a perfect 0.5 (middle) for our interpolation.

        Additionally, we precalculate a few other things to save time:
        - slope length of unit vector
        - u component of slope unit vector
        - v component of slope unit vector
        """
        pass

    def calc_du_dv(
        self,
        previous: CCTEntry,
        current: CCTEntry,
        factor: float
    ) -> tuple[float, float]:
        """Calculate the Duv."""
        pass

    def to_cct(self, color: Color, **kwargs: Any) -> Vector:
        """Calculate a color's CCT."""
        pass

    def from_cct(
        self,
        kelvin: float,
        duv: float,
        **kwargs: Any
    ) -> tuple[tuple[float, float], str]:
        """Calculate a color that satisfies the CCT."""
        pass
