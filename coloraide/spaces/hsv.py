"""HSV class."""
from __future__ import annotations
from .. import algebra as alg
from . import Space, HSVish
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from .. import util
from ..types import Vector
from typing import Any


def hsv_to_srgb(hsv: Vector) -> Vector:
    """
    Convert HSV to sRGB.

    https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB_alternative
    """
    pass


def srgb_to_hsv(rgb: Vector) -> Vector:
    """
    Convert sRGB to HSV.

    https://en.wikipedia.org/wiki/HSL_and_HSV#Hue_and_chroma
    https://en.wikipedia.org/wiki/HSL_and_HSV#Saturation
    https://en.wikipedia.org/wiki/HSL_and_HSV#Lightness
    """
    pass


class HSV(HSVish, Space):
    """HSL class."""

    BASE = "srgb"
    NAME = "hsv"
    SERIALIZE = ("--hsv",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, 1.0, bound=True),
        Channel("v", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "value": "v"
    }
    GAMUT_CHECK = "srgb"  # type: str | None
    CLIP_SPACE = "hsv"  # type: str | None
    WHITE = WHITES['2deg']['D65']

    def __init__(self, **kwargs: Any):
        """Initialize."""
        pass

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To HSL from HSV."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From HSL to HSV."""
        pass
