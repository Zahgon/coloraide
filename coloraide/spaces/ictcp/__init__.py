"""
ICtCp class.

https://professional.dolby.com/siteassets/pdfs/ictcp_dolbywhitepaper_v071.pdf
"""
from __future__ import annotations
from ..lab import Lab
from ...cat import WHITES
from ...channels import Channel, FLG_MIRROR_PERCENT
from ... import util
from ... import algebra as alg
from ...types import Vector

# All PQ Values are equivalent to defaults as stated in link below:
# https://en.wikipedia.org/wiki/High-dynamic-range_video#Perceptual_quantizer
#
# ```
# M1 = 2610 / 16384
# M1INV = 16384 / 2610
# M2 = 2523 / 32
# M2INV = 32 / 2523
# C1 = 3424 / 4096
# C2 = 2413 / 128
# C3 = 2392 / 128
# ```

# XYZ transform matrices
xyz_to_lms_m = [
    [0.3592832590121218, 0.6976051147779497, -0.0358915932320289],
    [-0.19208084637049927, 1.1004767970374318, 0.07537486585191187],
    [0.0070797844607477164, 0.07483966621863658, 0.8433265453898765]
]

lms_to_xyz_mi = [
    [2.0701522183894223, -1.3263473389671556, 0.20665104762940512],
    [0.36473852097480713, 0.6805660249472276, -0.04530454592203474],
    [-0.04974720753581203, -0.04926096669661379, 1.1880659249923042]
]

# LMS to Izazbz matrices
lms_p_to_ictcp_m = [
    [0.5, 0.5, 0.0],
    [1.61376953125, -3.323486328125, 1.709716796875],
    [4.378173828125, -4.24560546875, -0.132568359375]
]

ictcp_to_lms_p_mi = [
    [1.0, 0.008609037037932761, 0.11102962500302593],
    [1.0, -0.00860903703793275, -0.11102962500302599],
    [1.0, 0.5600313357106791, -0.32062717498731885]
]

YW = 203


def ictcp_to_xyz_d65(ictcp: Vector) -> Vector:
    """From ICtCp to XYZ."""
    pass


def xyz_d65_to_ictcp(xyzd65: Vector) -> Vector:
    """From XYZ to ICtCp."""
    pass


class ICtCp(Lab):
    """ICtCp class."""

    BASE = "xyz-d65"
    NAME = "ictcp"
    SERIALIZE = ("--ictcp", "ictcp")
    CHANNELS = (
        Channel("i", 0.0, 1.0),
        Channel("ct", -0.5, 0.5, flags=FLG_MIRROR_PERCENT),
        Channel("cp", -0.5, 0.5, flags=FLG_MIRROR_PERCENT)
    )
    CHANNEL_ALIASES = {
        "intensity": "i",
        "protan": "cp",
        "tritan": "ct"
    }
    WHITE = WHITES['2deg']['D65']
    DYNAMIC_RANGE = 'hdr'

    def lightness_name(self) -> str:
        """Get lightness name."""

        return "i"

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from ICtCp."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to ICtCp."""
        pass
