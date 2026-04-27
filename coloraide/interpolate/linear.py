"""Piecewise linear interpolation."""
from __future__ import annotations
import math
from .. import algebra as alg
from . import Interpolator, Interpolate
from ..types import Vector, AnyColor
from typing import Any


class InterpolatorLinear(Interpolator[AnyColor]):
    """Interpolate multiple ranges of colors using linear, Piecewise interpolation."""

    def normalize_hue(
        self,
        color1: Vector,
        color2: Vector,
        hue: str
    ) -> None:
        """
        Adjust hues.

        Undefined hues are not resolved at this point in time.
        When interpolating between achromatic colors, hue specifications
        such as shorter and longer will have no affect as undefined hues
        will remain undefined meaning there is no arc length to choose
        between. This gives more intuitive interpolation results.
        """
        pass


    def setup(self) -> None:
        """Setup for linear interpolation."""
        pass

    def interpolate(
        self,
        point: float,
        index: int
    ) -> Vector:
        """Interpolate."""
        pass


class Linear(Interpolate):
    """Linear interpolation plugin."""

    NAME = "linear"

    def interpolator(self, *args: Any, **kwargs: Any) -> Interpolator[AnyColor]:
        """Return the linear interpolator."""
        pass
