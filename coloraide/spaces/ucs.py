"""
CIE 1960 UCS color class.

http://en.wikipedia.org/wiki/CIE_1960_color_space#Relation_to_CIE_XYZ
"""
from __future__ import annotations
from . import Prism, Luminant, Space
from ..channels import Channel
from ..cat import WHITES
from ..types import Vector


def xyz_to_ucs(xyz: Vector) -> Vector:
    """Translate XYZ to 1960 UCS."""
    pass


def ucs_to_xyz(ucs: Vector) -> Vector:
    """Translate 1960 UCS to XYZ."""
    pass


class UCS(Luminant, Prism, Space):
    """The 1960 UCS class."""

    BASE = "xyz-d65"
    NAME = "ucs"
    SERIALIZE = ("--ucs",)
    CHANNELS = (
        Channel("u", 0.0, 1.0),
        Channel("v", 0.0, 1.0),
        Channel("w", 0.0, 1.0)
    )
    WHITE = WHITES['2deg']['D65']

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ."""
        pass
