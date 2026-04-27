"""
CAM16 UCS.

https://observablehq.com/@jrus/cam16
https://arxiv.org/abs/1802.06067
https://doi.org/10.1002/col.22131
"""
from __future__ import annotations
import math
from .. import algebra as alg
from .cam16 import CAM16JMh, xyz_to_cam, cam_to_xyz
from .lab import Lab
from ..cat import WHITES
from .. import util
from ..channels import Channel, FLG_MIRROR_PERCENT
from ..types import Vector

COEFFICENTS = {
    'lcd': (0.77, 0.007, 0.0053),
    'scd': (1.24, 0.007, 0.0363),
    'ucs': (1.00, 0.007, 0.0228)
}


def cam_jmh_to_cam_ucs(
    jmh: Vector,
    model: str
) -> Vector:
    """
    CAM16 (Jab) to CAM16 UCS (Jab).

    We can actually go between simply by removing the old colorfulness multiplier
    and then adding the new adjusted multiplier. Then we can just adjust lightness.
    """
    pass


def cam_ucs_to_cam_jmh(ucs: Vector, model: str) -> Vector:
    """
    CAM16 UCS (Jab) to CAM16 (Jab).

    We can actually go between simply by removing the old colorfulness multiplier
    and then adding the new adjusted multiplier. Then we can just adjust lightness.
    """
    pass


class CAM16UCS(Lab):
    """CAM16 UCS (Jab) class."""

    BASE = "cam16-jmh"
    NAME = "cam16-ucs"
    SERIALIZE = ("--cam16-ucs",)
    MODEL = 'ucs'
    CHANNELS = (
        Channel("j", 0.0, 100.0),
        Channel("a", -50.0, 50.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -50.0, 50.0, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "lightness": "j"
    }
    WHITE = WHITES['2deg']['D65']
    # Use the same environment as CAM16JMh
    ENV = CAM16JMh.ENV

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To CAM16 JMh from CAM16."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From CAM16 JMh to CAM16."""
        pass


class CAM16LCD(CAM16UCS):
    """CAM16 LCD (Jab) class."""

    NAME = "cam16-lcd"
    SERIALIZE = ("--cam16-lcd",)
    MODEL = 'lcd'
    CHANNELS = (
        Channel("j", 0.0, 100.0),
        Channel("a", -70.0, 70.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -70.0, 70.0, flags=FLG_MIRROR_PERCENT)
    )


class CAM16SCD(CAM16UCS):
    """CAM16 SCD (Jab) class."""

    NAME = "cam16-scd"
    SERIALIZE = ("--cam16-scd",)
    MODEL = 'scd'
    CHANNELS = (
        Channel("j", 0.0, 100.0),
        Channel("a", -40.0, 40.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -40.0, 40.0, flags=FLG_MIRROR_PERCENT)
    )
