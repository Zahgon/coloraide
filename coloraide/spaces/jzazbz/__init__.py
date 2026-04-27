"""
Jzazbz class.

https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-25-13-15131&id=368272

Relative XYZ has Y=100 for media white
BT.2048 says media white Y=203 at PQ 58, which is about 1000 cd/m^2.
This is confirmed here: https://www.itu.int/dms_pub/itu-r/opb/rep/R-REP-BT.2408-3-2019-PDF-E.pdf

If at some time that these assumptions are incorrect, we will be happy to alter the model.
"""
from __future__ import annotations
from ...cat import WHITES
from ...channels import Channel, FLG_MIRROR_PERCENT
from ... import util
from ... import algebra as alg
from ...types import Vector, Matrix  # noqa: F401
from ..lab import Lab

B = 1.15
G = 0.66
D = -0.56
D0 = 1.6295499532821566E-11
YW = 203

# All PQ Values are equivalent to defaults as stated in link below except `M2` (and `IM2`):
# https://en.wikipedia.org/wiki/High-dynamic-range_video#Perceptual_quantizer
#
# ```
# M1 = 2610 / (2 ** 14)
# IM1 = (2 ** 14) / 2610
# C1 = 3424 / (2 ** 12)
# C2 = 2413 / (2 ** 7)
# C3 = 2392 / (2 ** 7)
# M2 = 1.7 * 2523 / (2 ** 5)
# IM2 = (2 ** 5) / (1.7 * 2523)
# ```
M2 = 1.7 * 2523 / (2 ** 5)


# XYZ transform matrices
XYZ_TO_LMS = [
    [0.41478972, 0.579999, 0.014648],
    [-0.20151, 1.120649, 0.0531008],
    [-0.0166008, 0.2648, 0.6684799]
]

LMS_TO_XYZ = [
    [1.9242264357876069, -1.0047923125953657, 0.037651404030617994],
    [0.35031676209499907, 0.7264811939316552, -0.06538442294808501],
    [-0.09098281098284755, -0.31272829052307394, 1.5227665613052603]
]

# LMS to Izazbz matrices
LMS_P_TO_IZAZBZ = [
    [0.5, 0.5, 0],
    [3.524, -4.066708, 0.542708],
    [0.199076, 1.096799, -1.295875]
]

IZAZBZ_TO_LMS_P = [
    [1.0, 0.13860504327153927, 0.05804731615611883],
    [1.0, -0.1386050432715393, -0.058047316156118904],
    [1.0, -0.09601924202631895, -0.811891896056039]
]


def xyz_to_izazbz(xyz: Vector, lms_matrix: Matrix, m2: float) -> Vector:
    """Absolute XYZ to Izazbz."""
    pass


def izazbz_to_xyz(izazbz: Vector, lms_matrix: Matrix, m2: float) -> Vector:
    """Izazbz to absolute XYZ."""
    pass


def jzazbz_to_xyz(jzazbz: Vector) -> Vector:
    """From Jzazbz to XYZ."""
    pass


def xyz_to_jzazbz(xyz: Vector) -> Vector:
    """From XYZ to Jzazbz."""
    pass


class Jzazbz(Lab):
    """Jzazbz class."""

    BASE = "xyz-d65"
    NAME = "jzazbz"
    SERIALIZE = ("--jzazbz", "jzazbz")
    CHANNELS = (
        Channel("jz", 0.0, 1.0),
        Channel("az", -0.21, 0.21, flags=FLG_MIRROR_PERCENT),
        Channel("bz", -0.21, 0.21, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "lightness": 'jz',
        "a": 'az',
        "b": 'bz',
        "j": 'jz'
    }
    WHITE = WHITES['2deg']['D65']
    DYNAMIC_RANGE = 'hdr'

    def lightness_name(self) -> str:
        """Get lightness name."""

        return "jz"

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from Jzazbz."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to Jzazbz."""
        pass
