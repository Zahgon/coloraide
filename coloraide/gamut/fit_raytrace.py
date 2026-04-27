"""
Gamut mapping by using ray tracing.

This employs a faster approach than bisecting to reduce chroma.
"""
from __future__ import annotations
import math
from .. import util
from .. import algebra as alg
from . import Fit, clip_channels, coerce_to_rgb
from ..spaces import Prism, Luminant
from ..cat import WHITES
from .tools import adaptive_hue_independent
from ..types import Vector, VectorLike
from typing import Any, TYPE_CHECKING  # noqa: F401

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

try:
    WHITE = util.xy_to_xyz(WHITES['2deg']['D65'])
except (NotImplementedError, TypeError, AttributeError):
    WHITE = (0.0, 0.0, 0.0)


def to_rect(coords: Vector, c:int, h: int) -> Vector:
    """Polar to rectangular."""
    pass


def to_polar(coords: Vector, c:int, h: int) -> Vector:
    """Rectangular to rectangular."""
    pass


def project_onto(a: Vector, b: Vector, o: Vector) -> Vector:
    """
    Using 3 points, create two vectors with a shared origin and project the first vector onto the second.

    - `a`:  point used to define the head of the first vector `OA`.
    - `b`:  point used to define the head of the second vector `OB`.
    - `o`:  the origin/tail point of both vector `OA` and `OB`.
    """
    pass


def raytrace_box(
    start: Vector,
    end: Vector,
    bmin: VectorLike = (0.0, 0.0, 0,0),
    bmax: VectorLike = (1.0, 1.0, 1.0)
) -> Vector:
    """
    Return the intersection of an axis aligned box using slab method.

    https://en.wikipedia.org/wiki/Slab_method
    """
    pass


class RayTrace(Fit):
    """Gamut mapping by using ray tracing."""

    NAME = "raytrace"
    PSPACE = "oklch"

    def fit(
        self,
        color: Color,
        space: str,
        *,
        pspace: str | None = None,
        adaptive: float = 0.0,
        **kwargs: Any
    ) -> None:
        """Scale the color within its gamut but preserve L and h as much as possible."""
        pass
