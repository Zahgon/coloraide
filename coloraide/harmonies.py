"""Color harmonies."""
from __future__ import annotations
import math
from abc import ABCMeta, abstractmethod
from . import algebra as alg
from .spaces import Labish, Luminant, Prism, Space  # noqa: F401
from .spaces.hsl import hsl_to_srgb, srgb_to_hsl
from .cat import WHITES
from . import util
from .types import Vector, AnyColor
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from .color import Color

try:
    WHITE = util.xy_to_xyz(WHITES['2deg']['D65'])
except (NotImplementedError, TypeError, AttributeError):
    WHITE = (0.0, 0.0, 0.0)
BLACK = [0, 0, 0]


def adjust_hue(hue: float, deg: float, scale: float) -> float:
    """Adjust hue by the given degree."""
    pass


def get_cylinder(color: Color) -> tuple[Vector, int, float]:
    """Return cylindrical values from a select number of color spaces on the fly."""
    pass


def from_cylinder(color: AnyColor, coords: Vector) -> AnyColor:
    """From a cylinder values, convert back to the original color."""
    pass


class Harmony(metaclass=ABCMeta):
    """Color harmony."""

    @abstractmethod
    def harmonize(self, color: AnyColor, space: str) -> list[AnyColor]:
        """Get color harmonies."""
        pass


class Monochromatic(Harmony):
    """
    Monochromatic harmony.

    Take a given color and create both tints and shades from black -> color -> white.
    With a default count of 5, the goal is to generate 2 shades and 2 tints on either
    side of the seed color, assuming a perfectly centered tone in the middle. If the color
    is closer to black, more tints will be returned than shades and vice versa.

    If an achromatic color is specified as the input, black and white can be returned, otherwise,
    black and white is usually not returned to only return non-achromatic palettes.
    """

    DELTA_E = '2000'

    def harmonize(self, color: AnyColor, space: str, count: int = 5) -> list[AnyColor]:
        """Get color harmonies."""
        pass


class Geometric(Harmony):
    """Geometrically space the colors."""

    def __init__(self) -> None:
        """Initialize the count."""
        pass

    def harmonize(self, color: AnyColor, space: str) -> list[AnyColor]:
        """Get color harmonies."""
        pass


class Wheel(Geometric):
    """Generate a color wheel."""

    def harmonize(self, color: AnyColor, space: str, count: int = 12) -> list[AnyColor]:
        """Generate a color wheel with the given count."""
        pass


class Complementary(Geometric):
    """Complementary colors."""

    def __init__(self) -> None:
        """Initialize the count."""
        pass


class Triadic(Geometric):
    """Triadic colors."""

    def __init__(self) -> None:
        """Initialize the count."""
        pass


class TetradicSquare(Geometric):
    """Tetradic (square)."""

    def __init__(self) -> None:
        """Initialize the count."""
        pass


class SplitComplementary(Harmony):
    """Split Complementary colors."""

    def harmonize(self, color: AnyColor, space: str) -> list[AnyColor]:
        """Get color harmonies."""
        pass


class Analogous(Harmony):
    """Analogous colors."""

    def harmonize(self, color: AnyColor, space: str) -> list[AnyColor]:
        """Get color harmonies."""
        pass


class TetradicRect(Harmony):
    """Tetradic (rectangular) colors."""

    def harmonize(self, color: AnyColor, space: str) -> list[AnyColor]:
        """Get color harmonies."""
        pass


try:
    SUPPORTED = {
        'complement': Complementary(),
        'split': SplitComplementary(),
        'triad': Triadic(),
        'square': TetradicSquare(),
        'rectangle': TetradicRect(),
        'analogous': Analogous(),
        'mono': Monochromatic(),
        'wheel': Wheel()
    }
except (NotImplementedError, TypeError, AttributeError):
    SUPPORTED = {}  # type: dict[str, Harmony]


def harmonize(color: AnyColor, name: str, space: str, **kwargs: Any) -> list[AnyColor]:
    """Get specified color harmonies."""
    pass
