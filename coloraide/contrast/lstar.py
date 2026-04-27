"""
L* color contrast.

Used for color contrast in Google's HCT.

https://material.io/blog/science-of-color-design
"""
from __future__ import annotations
from . import ColorContrast
from ..types import AnyColor
from typing import Any


class LstarContrast(ColorContrast):
    """L* contrast."""

    NAME = "lstar"

    def contrast(self, color1: AnyColor, color2: AnyColor, **kwargs: Any) -> float:
        """Contrast."""
        pass
