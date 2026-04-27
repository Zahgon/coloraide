"""HSL class."""
from __future__ import annotations
from ... import algebra as alg
from .. import HSLish, Space
from ...cat import WHITES
from ...channels import Channel, FLG_ANGLE
from ... import util
from ...types import Vector
from typing import Any


def srgb_to_hsl(rgb: Vector) -> Vector:
    """
    Convert sRGB to HSL.

    https://en.wikipedia.org/wiki/HSL_and_HSV#Hue_and_chroma
    https://en.wikipedia.org/wiki/HSL_and_HSV#Saturation
    https://en.wikipedia.org/wiki/HSL_and_HSV#Lightness
    """
    pass


def hsl_to_srgb(hsl: Vector) -> Vector:
    """
    HSL to RGB.

    https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB_alternative
    """
    pass


class HSL(HSLish, Space):
    """HSL class."""

    BASE = "srgb"
    NAME = "hsl"
    SERIALIZE = ("--hsl",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, 1.0, bound=True),
        Channel("l", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "lightness": "l"
    }
    WHITE = WHITES['2deg']['D65']
    GAMUT_CHECK = "srgb"  # type: str | None
    CLIP_SPACE = "hsl"  # type: str | None

    def __init__(self, **kwargs: Any):
        """Initialize."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def is_achromatic(self, coords: Vector) -> bool | None:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB from HSL."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB to HSL."""
        pass
