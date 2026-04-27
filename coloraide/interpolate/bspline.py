"""
B-Spline interpolation.

https://en.wikipedia.org/wiki/B-spline
https://www.math.ucla.edu/~baker/149.1.02w/handouts/dd_splines.pdf
http://www2.cs.uregina.ca/~anima/408/Notes/Interpolation/UniformBSpline.htm
"""
from __future__ import annotations
from .. import algebra as alg
from .continuous import InterpolatorContinuous
from . import Interpolator, Interpolate
from ..types import Vector, AnyColor
from typing import Any


class InterpolatorBSpline(InterpolatorContinuous[AnyColor]):
    """Interpolate with B-spline."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize."""
        pass

    def setup(self) -> None:
        """Optional setup."""
        pass

    def interpolate(
        self,
        point: float,
        index: int
    ) -> Vector:
        """Interpolate."""
        pass


class BSpline(Interpolate):
    """B-spline interpolation plugin."""

    NAME = "bspline"

    def interpolator(self, *args: Any, **kwargs: Any) -> Interpolator[AnyColor]:
        """Return the B-spline interpolator."""
        pass
