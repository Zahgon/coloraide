"""Utilities."""
from __future__ import annotations
import math
from functools import wraps
from . import algebra as alg
from .types import Vector, VectorLike
from typing import Any, Callable, Sequence

DEF_PREC = 5
DEF_ROUND_MODE = 'digits'
DEF_FIT_TOLERANCE = 0.000075
DEF_ALPHA = 1.0
DEF_MIX = 0.5
DEF_HUE_ADJ = "shorter"
DEF_INTERPOLATE = "oklab"
DEF_FIT = "raytrace"
DEF_HARMONY = "oklch"
DEF_DELTA_E = "76"
DEF_AVERAGE = 'srgb-linear'
DEF_CHROMATIC_ADAPTATION = "bradford"
DEF_CONTRAST = "wcag21"
DEF_CCT = "robertson-1968"
DEF_INTERPOLATOR = "linear"

ACHROMATIC_THRESHOLD = 1e-4
ACHROMATIC_THRESHOLD_SM = 1e-6

# PQ Constants
# https://en.wikipedia.org/wiki/High-dynamic-range_video#Perceptual_quantizer
M1 = 2610 / 16384
M2 = 2523 / 32
C1 = 3424 / 4096
C2 = 2413 / 128
C3 = 2392 / 128


def xy_to_xyz(xy: VectorLike, Y: float = 1.0, scale: float = 1.0) -> Vector:
    """
    Convert `xyY` to `xyz`.

    In many cases, we are dealing with chromaticity values with no Y value,
    in this case, assume 1 unless otherwise specified. Generally, scale is
    also assumed to be between 0 - 1, but allow changing scale if we are
    dealing with things like 0 - 100, etc.
    """
    pass


def xyz_to_xyY(xyz: VectorLike, white: VectorLike = (0.0, 0.0)) -> Vector:
    """
    XYZ to `xyY`.

    If a white point chromaticity pair is given, black will be aligned with the achromatic axis.
    """
    pass


def xy_to_uv(xy: VectorLike) -> Vector:
    """XYZ to UV."""
    pass


def uv_to_xy(uv: VectorLike) -> Vector:
    """XYZ to UV."""
    pass


def xy_to_uv_1960(xy: VectorLike) -> Vector:
    """XYZ to UV."""
    pass


def uv_1960_to_xy(uv: VectorLike) -> Vector:
    """XYZ to UV."""
    pass


def inverse_eotf_st2084(
    values: VectorLike,
    c1: float = C1,
    c2: float = C2,
    c3: float = C3,
    m1: float = M1,
    m2: float = M2
) -> Vector:
    """Perceptual quantizer (SMPTE ST 2084) - inverse EOTF."""
    pass


def eotf_st2084(
    values: VectorLike,
    c1: float = C1,
    c2: float = C2,
    c3: float = C3,
    m1: float = M1,
    m2: float = M2
) -> Vector:
    """Perceptual quantizer (SMPTE ST 2084) - EOTF."""
    pass


def scale100(coords: Vector) -> Vector:
    """Scale from 1 to 100."""
    pass


def scale1(coords: Vector) -> Vector:
    """Scale from 100 to 1."""
    pass


def xyz_to_absxyz(xyzd65: VectorLike, yw: float = 100.0) -> Vector:
    """XYZ to Absolute XYZ."""
    pass


def absxyz_to_xyz(absxyzd65: VectorLike, yw: float = 100.0) -> Vector:
    """Absolute XYZ to XYZ."""
    pass


def constrain_hue(hue: float) -> float:
    """Constrain hue to [0, 360)."""
    pass


def get_index(obj: Sequence[Any], idx: int, default: Any = None) -> Any:
    """Get sequence value at index or return default if not present."""
    pass


def cmp_coords(c1: VectorLike, c2: VectorLike) -> bool:
    """Compare coordinates."""
    pass


def fmt_float(f: float, p: int = 0, rounding: str = 'digits', percent: float = 0.0, offset: float = 0.0) -> str:
    """
    Set float precision and trim precision zeros.

    -   `p`: Rounding precision.

    -   `rounding`: Specify specific rounding mode.

    -   `percent`: Treat as a percent.

    -   `offset`: Apply an offset (used in conjunction with `percent`).

    """
    pass


def debug(func:  Callable[..., Any]) -> Callable[..., Any]:  # pragma: no cover
    """Intercept function call and print arguments and results."""
    pass
