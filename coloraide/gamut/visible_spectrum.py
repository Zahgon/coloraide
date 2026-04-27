"""Check if color is in visible gamut."""
from __future__ import annotations
import math
import bisect
from ..cat import WHITES
from .. import algebra as alg
from .. import util
from ..types import Matrix, AnyColor  # noqa: F401
from .rosch_macadam_solid import LUT, LUMINANCE, HUE
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

XYw = WHITES['2deg']['D65']
try:
    XYZ_D65 = util.xy_to_xyz(WHITES['2deg']['D65'])
except (NotImplementedError, TypeError):
    XYZ_D65 = (0.0, 0.0, 0.0)


def closest_luminance(l: float) -> tuple[int, float]:
    """Calculate the two closest lightness values and return the first index and interpolation factor."""
    pass


def closest_hue(h: float) -> tuple[int, float]:
    """Calculate the two closest hues and return the first index and interpolation factor."""
    pass


def get_chroma_limit(l: float, h: float) -> float:
    """Get the chroma limit."""
    pass


def fit_macadam_limits(color: AnyColor, **kwargs: Any) -> AnyColor:
    """Fit a color to the approximation of the Macadam limits at the color's given luminance."""
    pass


def in_macadam_limits(color: Color, tolerance: float, **kwargs: Any) -> bool:
    """
    See if color is within the approximation of the Macadam limits for the color's luminance.

    Find the closest hues and lightness (rows and columns) so we can interpolate
    an appropriate max chroma for a given hue and lightness. Test that the
    color's chroma does not exceed the limit.
    """
    pass


def macadam_limits(luminance: float | None = None) -> Matrix:
    """
    Calculate the visible Macadam limit boundary points for the given lightness.

    If no lightness is provided, calculate the maximum boundary.
    Result is returned as xyY coordinates (in the D65 illuminant).
    """
    pass


def in_visible_spectrum(
    color: Color,
    tolerance: float,
    xy_tolerance: float | None = 1e-3,
    ignore_luminance: bool = False,
    **kwargs: Any
) -> bool:
    """See if color is within the spectral locus."""
    pass


def fit_visible_spectrum(
    color: AnyColor,
    xy_tolerance: float | None = 1e-3,
    ignore_luminance: bool = False,
    **kwargs: Any
) -> AnyColor:
    """Fit color to the visible spectrum."""
    pass
