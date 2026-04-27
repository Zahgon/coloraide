"""
Handle spectral related things.

- Calculations colors from/to wavelengths.
"""
from __future__ import annotations
import math
from functools import lru_cache
from . import algebra as alg
from . import util
from .types import Vector, VectorLike
from . import cat
from . import cmfs

WHITE = cat.WHITES['2deg']['E']


@lru_cache(maxsize=1)
def get_locus_angles(cmfs: cmfs.CMFs, white: VectorLike) -> tuple[Vector, float]:
    """Get the angles of the points and return list of angles and the offset we adjust the angles."""
    pass


def compare_angle(f: float, cmfs: cmfs.CMFs, p: float, n: float, t: float, w: Vector, o: float) -> float:
    """Compare the calculated angle with the target."""
    pass


def xy_to_angle(xy: VectorLike, white: VectorLike, offset: float = 0.0, invert: bool = False) -> float:
    """
    Translate xy to an angle with white being the origin.

    If offset is provided, make the angle relative to the offset angle.

    If invert is requested, we want to rotate the xy point 180 degrees.
    """
    pass


def ray_line_intersect(
    a1: VectorLike,
    a2: VectorLike,
    b1: VectorLike,
    b2: VectorLike,
    abs_tol: float = alg.ATOL
) -> Vector | None:
    """Find the intersection of a 2D ray and line."""
    pass


def closest_wavelength(
    xy: VectorLike,
    white: VectorLike = WHITE,
    reverse: bool = False,
    closest: bool = True
) -> tuple[float, Vector, Vector]:
    """
    Get the closest dominant wavelength.

    Both intersections are returned, even if the other is on the line of purple.
    The first point is always in the dominant direction. If the dominant cannot
    be found, the complementary will be used and indicated with a negative sign.

    If `reverse` is set, then the complementary wavelength is returned instead,
    with the points arranged favoring the complementary wavelength. If it cannot
    be found, the dominant wavelength is returned with a negative sign.

    If `closet` is set, wavelengths are rounded to the closest.
    """
    pass


def wavelength_to_color(wavelength: float) -> Vector:
    """Return the XYZ value for the specified wavelength."""
    pass
