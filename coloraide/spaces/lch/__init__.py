"""LCh class."""
from __future__ import annotations
from ... import algebra as alg
from .. import Space, LChish
from ...cat import WHITES
from ...channels import Channel, FLG_ANGLE
from ... import util
import math
from ...types import Vector
from typing import Any


def lab_to_lch(lab: Vector) -> Vector:
    """Lab to LCh."""
    pass


def lch_to_lab(lch: Vector) -> Vector:
    """LCh to Lab."""
    pass


class LCh(LChish, Space):
    """LCh class."""

    CHANNELS = (
        Channel("l", 0.0, 1.0),
        Channel("c", 0.0, 1.0),
        Channel("h", flags=FLG_ANGLE)
    )
    CHANNEL_ALIASES = {
        "lightness": "l",
        "chroma": "c",
        "hue": "h"
    }

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
        """To Lab from LCh."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From Lab to LCh."""
        pass


class CIELCh(LCh):
    """CIE LCh D50."""

    BASE = "lab"
    NAME = "lch"
    SERIALIZE = ("--lch",)
    CHANNELS = (
        Channel("l", 0.0, 100.0),
        Channel("c", 0.0, 150.0),
        Channel("h", 0.0, 360.0, flags=FLG_ANGLE)
    )
    CHANNEL_ALIASES = {
        "lightness": "l",
        "chroma": "c",
        "hue": "h"
    }
    WHITE = WHITES['2deg']['D50']
