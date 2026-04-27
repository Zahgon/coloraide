"""
Simple Color Appearance Model (sCAM).

https://opg.optica.org/oe/fulltext.cfm?uri=oe-32-3-3100&id=545619
"""
from __future__ import annotations
import math
from .. import util
from .. import algebra as alg
from .lch import LCh
from ..channels import Channel, FLG_ANGLE
from .cam16 import M16, M16_INV, hue_quadrature, inv_hue_quadrature
from .sucs import xyz_to_sucs, sucs_to_xyz
from ..cat import WHITES
from ..types import Vector, VectorLike

SURROUND = {
    'dark': (0.39, 0.85),
    'dim': (0.5, 0.95),
    'average': (0.52, 1)
}

HUE_QUADRATURE = {
    # Red, Yellow, Green, Blue, Red
    "h": (15.6, 80.3, 157.8, 219.7, 376.6),
    "e": (0.7, 0.6, 1.2, 0.9, 0.7),
    "H": (0.0, 100.0, 200.0, 300.0, 400.0)
}


def eccentricity(h: float) -> float:
    """Calculate eccentricity."""
    pass


def adapt(xyz: Vector, xyz_ws: Vector, xyz_wd: Vector, d: float) -> Vector:
    """
    Adapt using CAT16 matrix but using CAM02 degree of adaptation.

    This was proposed by one of the authors Li, Molin in the Colour project:
    https://github.com/colour-science/colour/pull/1349#issuecomment-3058339414
    """
    pass


class Environment:
    """
    Class to calculate and contain any required environmental data (viewing conditions included).

    Usage Guidelines for CIECAM97s (Nathan Moroney)
    https://www.researchgate.net/publication/220865484_Usage_guidelines_for_CIECAM97s

    `white`: This is the (x, y) chromaticity points for the white point. This should be the same
        value as set in the color class `WHITE` value.

    `adapting_luminance`: This is the luminance of the adapting field. The units are in cd/m2.
        The equation is `L = (E * R) / π`, where `E` is the illuminance in lux, `R` is the reflectance,
        and `L` is the luminance. If we assume a perfectly reflecting diffuser, `R` is assumed as 1.
        For the "gray world" assumption, we must also divide by 5 (or multiply by 0.2 - 20%).
        This results in `La = E / π * 0.2`. You can also ignore this gray world assumption converting
        lux directly to nits (cd/m2) `lux / π`.

    `background_luminance`: The background is the region immediately surrounding the stimulus and
        for images is the neighboring portion of the image. Generally, this value is set to a value of 20.
        This implicitly assumes a gray world assumption.

    `surround`: The surround is categorical and is defined based on the relationship between the relative
        luminance of the surround and the luminance of the scene or image white. While there are 4 defined
        surrounds, usually just `average`, `dim`, and `dark` are used.

        Dark    | 0%        | Viewing film projected in a dark room
        Dim     | 0% to 20% | Viewing television
        Average | > 20%     | Viewing surface colors

    `discounting`: Whether we are discounting the illuminance. Done when eye is assumed to be fully adapted.
    """

    def __init__(
        self,
        *,
        white: VectorLike,
        adapting_luminance: float,
        background_luminance: float,
        surround: str,
        discounting: bool
    ):
        """
        Initialize environmental viewing conditions.

        Using the specified viewing conditions, and general environmental data,
        initialize anything that we can ahead of time to speed up the process.
        """
        pass


def scam_to_xyz(
    J: float | None = None,
    C: float | None = None,
    h: float | None = None,
    Q: float | None = None,
    M: float | None = None,
    D: float | None = None,
    V: float | None = None,
    W: float | None = None,
    K: float | None = None,
    H: float | None = None,
    env: Environment | None = None
) -> Vector:
    """
    From sCAM to XYZ.

    Reverse calculation can actually be obtained from a small subset of the sCAM components
    Really, only one suitable value is needed for each type of attribute: (lightness/brightness),
    (chroma/colorfulness/depth/vividness/whiteness/blackness), (hue/hue quadrature). If more than one for a given
    category is given, we will fail as we have no idea which is the right one to use. Also,
    if none are given, we must fail as well as there is nothing to calculate with.
    """
    pass


def xyz_to_scam(xyz: Vector, env: Environment, calc_hue_quadrature: bool = False) -> Vector:
    """From XYZ to sCAM."""
    pass


def xyz_to_scam_jmh(xyz: Vector, env: Environment) -> Vector:
    """XYZ to sCAM JMh."""
    pass


def scam_jmh_to_xyz(jmh: Vector, env: Environment) -> Vector:
    """Convert sCAM JMh to XYZ."""
    pass


class sCAMJMh(LCh):
    """sCAM class (JMh)."""

    BASE = "xyz-d65"
    NAME = "scam-jmh"
    SERIALIZE = ("--scam-jmh",)
    CHANNEL_ALIASES = {
        "lightness": "j",
        "colorfulness": 'm',
        "hue": 'h'
    }
    WHITE = WHITES['2deg']['D65']
    # Assuming sRGB which has a lux of 64: `((E * R) / PI) / 5` where `R = 1`.
    ENV = Environment(
        # Our white point.
        white=WHITE,
        # Assuming sRGB which has a lux of 64: `((E * R) / PI)` where `R = 1`.
        # Divided by 5 (or multiplied by 20%) assuming gray world.
        adapting_luminance=64 / math.pi * 0.2,
        # Gray world assumption, 20% of reference white's `Yw = 100`.
        background_luminance=20,
        # Average surround
        surround='average',
        # Do not discount illuminant
        discounting=False
    )
    CHANNELS = (
        Channel("j", 0.0, 100.0),
        Channel("m", 0, 25.0),
        Channel("h", 0.0, 360.0, flags=FLG_ANGLE)
    )

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def radial_name(self) -> str:
        """Get radial name."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """Normalize."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """From sCAM JMh to XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to sCAM JMh."""
        pass
