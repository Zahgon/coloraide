"""Continuous interpolation."""
from __future__ import annotations
import math
from .. import algebra as alg
from . import Interpolator, Interpolate
from ..types import Vector, AnyColor
from typing import Any


def adjust_shorter(h1: float, h2: float, offset: float, mx: float) -> tuple[float, float]:
    """Adjust the given hues such that they favor the shorter arc."""
    pass


def adjust_longer(h1: float, h2: float, offset: float, mx: float) -> tuple[float, float]:
    """Adjust the given hues such that they favor the longer arc."""
    pass


def adjust_increase(h1: float, h2: float, offset: float, mx: float) -> tuple[float, float]:
    """Adjust the given hues such that they are increasing."""
    pass


def adjust_decrease(h1: float, h2: float, offset: float, mx: float) -> tuple[float, float]:
    """Adjust the given hues such that they are decreasing."""
    pass


class InterpolatorContinuous(Interpolator[AnyColor]):
    """Interpolate with continuous piecewise."""

    def normalize_hue(
        self,
        color1: Vector,
        color2: Vector | None,
        offset: float,
        hue: str,
        fallback: float | None
    ) -> tuple[Vector, float]:
        """
        Normalize hues according the hue specifier.

        Hues are normalized in a continuous way such that the fix-up is applied
        relative to the hues that come before it.
        """
        pass

    def handle_undefined(self) -> None:
        """
        Handle null values.

        Resolve any undefined alpha values and apply premultiplication if necessary.

        Additionally, any undefined value have a new control point generated via
        linear interpolation. This is the only approach to provide a non-bias, non-breaking
        way to handle things like achromatic hues in a cylindrical space. It also balances
        non cylindrical values. Since the B-spline needs a a continual path and since we
        have a sliding window that takes into account 4 points at a time, we must consider
        a more broad context than what is done in piecewise linear.
        """
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


class Continuous(Interpolate):
    """Continuous interpolation plugin."""

    NAME = "continuous"

    def interpolator(self, *args: Any, **kwargs: Any) -> Interpolator[AnyColor]:
        """Return the continuous interpolator."""
        pass
