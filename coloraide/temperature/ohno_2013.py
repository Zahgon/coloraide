"""
Ohno 2013 CCT calculations.

https://www.researchgate.net/publication/263373260_Practical_Use_and_Calculation_of_CCT_and_Duv
"""
from __future__ import annotations
import math
from . import planck
from .. import cat
from .. import cmfs
from .. import util
from .. import algebra as alg
from . import CCT
from ..types import Vector, VectorLike
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color


class BlackBodyCurve:
    """
    Setup a spline that represents the black body curve.

    Points between steps are approximated, but actual points can always be
    acquired via `exact`.

    For improved accuracy, we split spline data for low temps and high temps
    and assign the number of required data points accordingly.
    """

    def __init__(
        self,
        cmfs: cmfs.CMFs = cmfs.CIE_1931_2DEG,
        white: VectorLike = cat.WHITES['2deg']['D65'],
        planck_step: int = 5,
        chromaticity: str = 'uv-1960'
    ) -> None:
        """Initialize."""
        pass

    def __call__(self, temp: float, exact: bool = False) -> Vector:
        """Get the uv for the given temp."""
        pass


class Ohno2013(CCT):
    """
    Calculate temperature for a given pair of uv coordinates.

    The Ohno approach requires a pre-generated table. The more data available, the more precise the values.
    Unfortunately, to span the entire range of 1000 - 100000 with fairly good accuracy, it requires keeping
    a very large table in memory.

    To avoid storing a large amount of data in memory, we can use multiple iterations and dynamically sample
    points on the locus, each iteration shrinking the bounds until we converge. Unfortunately, this is very
    slow, millisecond range.

    An alternative is to use the iterative approach, but generate a smaller subset of data and use a spline
    to approximate the points in between. Obviously, the points in between will not be as accurate, but the
    spline is used only as a way to approximate close to the temperature. Once we've sufficiently narrowed
    the range down to our best 3 temperature points, we can calculate those points with higher accuracy and
    proceed with the solvers. This actually allows us to use an even smaller amount of data than if we had
    used no spline and pre-calculated enough points for a similar accuracy. This is also much faster than
    dynamically calculating all the points.

    After navigating the table of data and determining a temperature that has the lowest delta distance, we can
    then use the triangular and parabolic solver. The triangular works best for values close to the locus (less
    than |0.002| Duv) and the parabolic solution works better for values with a higher Duv.

    For more precision, `exact` will avoid the approximation spline.

    https://www.researchgate.net/publication/263373260_Practical_Use_and_Calculation_of_CCT_and_Duv
    """

    NAME = 'ohno-2013'
    CHROMATICITY = 'uv-1960'

    def __init__(
        self,
        cmfs: cmfs.CMFs = cmfs.CIE_1931_2DEG,
        white: VectorLike = cat.WHITES['2deg']['D65'],
        planck_step: int = 5
    ):
        """Initialize."""
        pass

    def to_cct(
        self,
        color: Color,
        start: float = 1000,
        end: float = 100000,
        samples: int = 10,
        iterations: int = 6,
        exact: bool = False,
        **kwargs: Any
    ) -> Vector:
        """Calculate a color's CCT."""
        pass

    def from_cct(
        self,
        kelvin: float,
        duv: float,
        **kwargs: Any
    ) -> tuple[tuple[float, float], str]:
        """Calculate a color that satisfies the CCT using Planck's law."""
        pass
