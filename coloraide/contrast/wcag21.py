"""
WCAG 2.1 contrast ratio.

https://www.w3.org/TR/WCAG20/#contrast-ratiodef
"""
from __future__ import annotations
from . import ColorContrast
from ..types import AnyColor
from typing import Any


class WCAG21Contrast(ColorContrast):
    """WCAG 2.1 contrast ratio."""

    NAME = "wcag21"

    def contrast(self, color1: AnyColor, color2: AnyColor, **kwargs: Any) -> float:
        """Contrast."""
        pass
