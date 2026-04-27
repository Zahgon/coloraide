"""
Hunter Lab class.

https://support.hunterlab.com/hc/en-us/articles/203997095-Hunter-Lab-Color-Scale-an08-96a2
"""
from __future__ import annotations
from ..cat import WHITES
from .lab import Lab
from .. import algebra as alg
from .. import util
from ..types import Vector, VectorLike
from ..channels import Channel, FLG_MIRROR_PERCENT

# Values for the original Hunter Lab with illuminant C.
# Used to calculate an appropriate `Ka` and `Kb` for whatever white point we are using.
CXN = 98.04
CYN = 100.0
CZN = 118.11
CKA = 175.0
CKB = 70.0


def xyz_to_hlab(xyz: Vector, white: VectorLike) -> Vector:
    """Convert XYZ to Hunter Lab."""
    pass


def hlab_to_xyz(hlab: Vector, white: VectorLike) -> Vector:
    """Convert Hunter Lab to XYZ."""
    pass


class HunterLab(Lab):
    """Hunter Lab class."""

    BASE = 'xyz-d65'
    NAME = "hunter-lab"
    SERIALIZE = ("--hunter-lab",)
    WHITE = WHITES['2deg']['D65']
    CHANNELS = (
        Channel("l", 0.0, 100.0),
        Channel("a", -210.0, 210.0, flags=FLG_MIRROR_PERCENT),
        Channel("b", -210.0, 210.0, flags=FLG_MIRROR_PERCENT)
    )

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Hunter Lab."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Hunter Lab."""
        pass
