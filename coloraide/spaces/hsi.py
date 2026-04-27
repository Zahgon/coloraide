"""
HSI class.

https://en.wikipedia.org/wiki/HSL_and_HSV#Saturation
"""
from __future__ import annotations
import math
from .hsv import HSV
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from .. import util
from ..types import Vector


def srgb_to_hsi(rgb: Vector) -> Vector:
    """Convert sRGB to HSI."""
    pass


def hsi_to_srgb(hsi: Vector) -> Vector:
    """HSI to RGB."""
    pass


class HSI(HSV):
    """HSI class."""

    BASE = "srgb"
    NAME = "hsi"
    SERIALIZE = ("--hsi",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, 1.0, bound=True),
        Channel("i", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "intensity": "i"
    }
    WHITE = WHITES['2deg']['D65']
    GAMUT_CHECK = "srgb"
    CLIP_SPACE = None

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To sRGB from HSI."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From sRGB to HSI."""
        pass
