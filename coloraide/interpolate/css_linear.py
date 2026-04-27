"""Piecewise linear interpolation."""

from __future__ import annotations
from .linear import InterpolatorLinear
from . import Interpolator, Interpolate
from ..types import AnyColor
from ..deprecate import deprecated
from typing import Any


class CSSLinear(Interpolate):
    """CSS Linear interpolation plugin."""

    NAME = "css-linear"

    def interpolator(self, *args: Any, **kwargs: Any) -> Interpolator[AnyColor]:  # pragma: no cover
        """Return the CSS linear interpolator."""
        pass
