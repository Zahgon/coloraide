"""Gamut handling."""
from __future__ import annotations
import math
from abc import ABCMeta, abstractmethod
from functools import lru_cache
from . import pointer
from . import visible_spectrum
from .. import util
from .. import algebra as alg
from ..channels import FLG_ANGLE
from ..types import Plugin, Vector, VectorLike
from ..spaces import Prism, Luminant, Space, HSLish, HSVish, HWBish
from ..spaces.hsl import hsl_to_srgb, srgb_to_hsl
from ..spaces.hsv import hsv_to_srgb, srgb_to_hsv
from ..spaces.hwb import hwb_to_hsv, hsv_to_hwb
from ..spaces.srgb_linear import sRGBLinear
from typing import Any, TYPE_CHECKING, Callable  # noqa: F401

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

__all__ = ('clip_channels', 'verify', 'Fit', 'pointer', 'visible_spectrum', 'scale_rgb', 'coerce_to_rgb')

SPECIAL_GAMUTS = {
    'pointer-gamut': {
        'check': pointer.in_pointer_gamut,
        'fit': pointer.fit_pointer_gamut
    },
    'macadam-limits': {
        'check': visible_spectrum.in_macadam_limits,
        'fit': visible_spectrum.fit_macadam_limits
    },
    'visible-spectrum': {
        'check': visible_spectrum.in_visible_spectrum,
        'fit': visible_spectrum.fit_visible_spectrum
    }
}   # type: dict[str, dict[str, Callable[..., Any]]]


def hwb_to_srgb(coords: Vector) -> Vector:  # pragma: no cover
    """Convert HWB to sRGB."""
    pass


def srgb_to_hwb(coords: Vector) -> Vector:  # pragma: no cover
    """Convert sRGB to HWB."""
    pass


@lru_cache(maxsize=20, typed=True)
def coerce_to_rgb(cs: Space) -> Space:
    """
    Coerce an HSL, HSV, or HWB color space to RGB to allow us to ray trace the gamut.

    It is rare to have a color space that is bound to an RGB gamut that does not exist as an RGB
    defined RGB space. HPLuv is one that is defined only as a cylindrical, HSL-like space. Okhsl
    and Okhsv are another whose gamut is meant to target sRGB, but it is very fuzzy and has sRGB
    colors not quite in gamut, and others that exceed the sRGB gamut.

    For gamut mapping, RGB cylindrical spaces can be coerced into an RGB form using traditional
    HSL, HSV, or HWB approaches which is good enough.
    """
    pass


def adjust_luminance(
    color: Color,
    Y: float,
    white: VectorLike,
    max_luminance: float = 1.0,
    preserve_luminance: bool = True
) -> None:
    """Adjust luminance of a color."""
    pass


def scale_rgb(
    color: Color,
    *,
    scale_space: str,
    clip_negative: bool = False,
    max_saturation: bool = False,
    preserve_luminance: bool = False
) -> None:
    """Apply color scaling."""
    pass


def clip_channels(color: Color, nans: bool = True) -> bool:
    """Clip channels."""
    pass


def verify(color: Color, tolerance: float) -> bool:
    """Verify the values are in bound."""
    pass


class Fit(Plugin, metaclass=ABCMeta):
    """Fit plugin class."""

    NAME = ''

    @abstractmethod
    def fit(self, color: Color, space: str, **kwargs: Any) -> None:
        """Get coordinates of the new gamut mapped color."""
