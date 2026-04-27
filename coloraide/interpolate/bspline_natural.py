"""
Natural B-Spline interpolation.

https://www.math.ucla.edu/~baker/149.1.02w/handouts/dd_splines.pdf.
"""
from __future__ import annotations
from . import Interpolate, Interpolator
from .bspline import InterpolatorBSpline
from .. import algebra as alg
from .. types import AnyColor
from typing import Any


class InterpolatorNaturalBSpline(InterpolatorBSpline[AnyColor]):
    """Natural B-spline class."""

    def setup(self) -> None:
        """Setup."""
        pass


class NaturalBSpline(Interpolate):
    """Natural B-spline interpolation plugin."""

    NAME = "natural"

    def interpolator(self, *args: Any, **kwargs: Any) -> Interpolator[AnyColor]:
        """Return the natural B-spline interpolator."""
        pass
