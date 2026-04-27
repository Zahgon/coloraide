"""Blend modes."""
from __future__ import annotations
import math
from abc import ABCMeta, abstractmethod
from operator import itemgetter
from ..types import Vector


# -----------------------------------------
# Non-separable blending helper functions
# -----------------------------------------
def lum(rgb: Vector) -> float:
    """Get luminosity."""
    pass


def clip_color(rgb: Vector) -> Vector:
    """Clip color."""
    pass


def set_lum(rgb: Vector, l: float) -> Vector:
    """Set luminosity."""
    pass


def sat(rgb: Vector) -> float:
    """Saturation."""
    pass


def set_sat(rgb: Vector, s: float) -> Vector:
    """Set saturation."""
    pass


# -----------------------------------------
# Blend modes
# -----------------------------------------
class Blend(metaclass=ABCMeta):
    """Blend base class."""

    @abstractmethod
    def blend(self, coords1: Vector, coords2: Vector) -> Vector:  # pragma: no cover
        """Blend coordinates."""
        pass


class SeperableBlend(Blend):
    """Blend coordinates."""

    @abstractmethod
    def apply(self, cb: float, cs: float) -> float:  # pragma: no cover
        """Blend two values."""
        pass

    def blend(self, coords1: Vector, coords2: Vector) -> Vector:
        """Apply blending logic."""
        pass


class NonSeperableBlend(Blend):
    """Non seperable blend method."""

    @abstractmethod
    def apply(self, cb: Vector, cs: Vector) -> Vector:  # pragma: no cover
        """Blend two vectors."""
        pass

    def blend(self, coords1: Vector, coords2: Vector) -> Vector:
        """Apply blending logic."""
        pass


class BlendNormal(SeperableBlend):
    """Normal blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendMultiply(SeperableBlend):
    """Multiply blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendScreen(SeperableBlend):
    """Screen blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendDarken(SeperableBlend):
    """Darken blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendLighten(SeperableBlend):
    """Lighten blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendColorDodge(SeperableBlend):
    """Color dodge blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendColorBurn(SeperableBlend):
    """Color Burn blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendOverlay(SeperableBlend):
    """Overlay blend mode."""

    def __init__(self) -> None:
        """Initialize."""
        pass

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendDifference(SeperableBlend):
    """Difference blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendExclusion(SeperableBlend):
    """Exclusion blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendHardLight(SeperableBlend):
    """Hard light blend mode."""

    def __init__(self) -> None:
        """Initialize."""
        pass

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendSoftLight(SeperableBlend):
    """Soft light blend mode."""

    def apply(self, cb: float, cs: float) -> float:
        """Blend two values."""
        pass


class BlendHue(NonSeperableBlend):
    """Hue blend mode."""

    def apply(self, cb: Vector, cs: Vector) -> Vector:
        """Blend two vectors."""
        pass


class BlendSaturation(NonSeperableBlend):
    """Saturation blend mode."""

    def apply(self, cb: Vector, cs: Vector) -> Vector:
        """Blend two vectors."""
        pass


class BlendLuminosity(NonSeperableBlend):
    """Luminosity blend mode."""

    def apply(self, cb: Vector, cs: Vector) -> Vector:
        """Blend two vectors."""
        pass


class BlendColor(NonSeperableBlend):
    """Color blend mode."""

    def apply(self, cb: Vector, cs: Vector) -> Vector:
        """Blend two vectors."""
        pass


try:
    SUPPORTED = {
        "normal": BlendNormal(),
        "multiply": BlendMultiply(),
        "screen": BlendScreen(),
        "darken": BlendDarken(),
        "lighten": BlendLighten(),
        "color-dodge": BlendColorDodge(),
        "color-burn": BlendColorBurn(),
        "overlay": BlendOverlay(),
        "difference": BlendDifference(),
        "exclusion": BlendExclusion(),
        "hard-light": BlendHardLight(),
        "soft-light": BlendSoftLight(),
        "hue": BlendHue(),
        "saturation": BlendSaturation(),
        "luminosity": BlendLuminosity(),
        "color": BlendColor(),
    }
except (NotImplementedError, TypeError, AttributeError):
    SUPPORTED = {}  # type: dict[str, Blend]


def get_blender(blend: str) -> Blend:
    """Get desired blend mode."""
    pass
