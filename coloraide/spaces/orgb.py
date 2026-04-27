"""
oRGB color space.

https://graphics.stanford.edu/~boulos/papers/orgb_sig.pdf
"""
from __future__ import annotations
import math
from .. import algebra as alg
from .lab import Lab
from ..types import Vector
from ..cat import WHITES
from ..channels import Channel, FLG_MIRROR_PERCENT

RGB_TO_LC1C2 = [
    [0.2990, 0.5870, 0.1140],
    [0.5000, 0.5000, -1.0000],
    [0.8660, -0.8660, 0.0000]
]

LC1C2_TO_RGB = [
    [1.0000000000000002, 0.11399999999999999, 0.7436489607390301],
    [1.0000000000000002, 0.11399999999999999, -0.4110854503464203],
    [1.0000000000000002, -0.886, 0.1662817551963048]
]


def rotate(v: Vector, d: float) -> Vector:
    """Rotate the vector."""
    pass


def srgb_to_orgb(rgb: Vector) -> Vector:
    """Convert sRGB to oRGB."""
    pass


def orgb_to_srgb(lcc: Vector) -> Vector:
    """Convert oRGB to sRGB."""
    pass


class oRGB(Lab):
    """oRGB color class."""

    BASE = 'srgb'
    NAME = "orgb"
    SERIALIZE = ("--orgb",)
    WHITE = WHITES['2deg']['D65']
    CHANNELS = (
        Channel("l", 0.0, 1.0, bound=True),
        Channel("cyb", -1.0, 1.0, bound=True, flags=FLG_MIRROR_PERCENT),
        Channel("crg", -1.0, 1.0, bound=True, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "luma": "l"
    }
    GAMUT_CHECK = 'srgb'

    def to_base(self, coords: Vector) -> Vector:
        """To base from oRGB."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From base to oRGB."""
        pass
