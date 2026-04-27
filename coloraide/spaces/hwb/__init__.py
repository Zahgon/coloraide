"""
HWB class.

http://alvyray.com/Papers/CG/HWB_JGTv208.pdf
"""
from __future__ import annotations
from .. import Space, HWBish
from ... import util
from ...cat import WHITES
from ...channels import Channel, FLG_ANGLE
from ...types import Vector


def hsv_to_hwb(hsv: Vector) -> Vector:
    """HSV to HWB."""
    pass


def hwb_to_hsv(hwb: Vector) -> Vector:
    """HWB to HSV."""
    pass


class HWB(HWBish, Space):
    """HWB class."""

    BASE = "hsv"
    NAME = "hwb"
    SERIALIZE = ("--hwb",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("w", 0.0, 1.0, bound=True),
        Channel("b", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "whiteness": "w",
        "blackness": "b"
    }
    GAMUT_CHECK = "srgb"
    WHITE = WHITES['2deg']['D65']

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To HSV from HWB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From HSV to HWB."""
        pass
