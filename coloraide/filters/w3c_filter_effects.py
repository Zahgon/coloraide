"""Provide filters as described by the https://www.w3.org/TR/filter-effects-1/."""
from __future__ import annotations
import math
from . import Filter
from .. import algebra as alg
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color


def linear_transfer(value: float, slope: float = 1.0, intercept: float = 0.0) -> float:
    """
    Linear transfer function.

    https://drafts.fxtf.org/filter-effects-1/#feFuncRElement
    """
    pass


class Sepia(Filter):
    """Sepia filter."""

    NAME = 'sepia'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a sepia filter to the color."""
        pass


class Grayscale(Filter):
    """Grayscale filter."""

    NAME = 'grayscale'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a grayscale filter to the color."""
        pass


class Saturate(Filter):
    """Saturation filter."""

    NAME = 'saturate'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a saturation filter to the color."""
        pass


class Invert(Filter):
    """Invert filter."""

    NAME = 'invert'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply an invert filter."""
        pass


class Opacity(Filter):
    """Opacity filter."""

    NAME = 'opacity'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply an opacity filter."""
        pass


class Brightness(Filter):
    """Brightness filter."""

    NAME = 'brightness'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a brightness filter."""
        pass


class Contrast(Filter):
    """Contrast filter."""

    NAME = 'contrast'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a contrast filter."""
        pass


class HueRotate(Filter):
    """Hue rotate filter."""

    NAME = 'hue-rotate'
    ALLOWED_SPACES = ('srgb-linear', 'srgb')

    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Apply a hue rotation filter."""
        pass
