"""
Hellwig 2022: CAM16 class (JMh) with corrections.

CAM16
https://www.researchgate.net/publication/318152296_Comprehensive_color_solutions_CAM16_CAT16_and_CAM16-UCS
https://www.researchgate.net/publication/220865484_Usage_guidelines_for_CIECAM97s
https://doi.org/10.1002/col.22131
https://observablehq.com/@jrus/cam16
https://arxiv.org/abs/1802.06067

CAM16 Corrections: Hellwig and Fairchild
http://markfairchild.org/PDFs/PAP45.pdf

Helmholtz Kohlrausch Effect extension: Hellwig, Stolitzka, and Fairchild
https://www.scribd.com/document/788387893/Color-Research-Application-2022-Hellwig-Extending-CIECAM02-and-CAM16-for-the-Helmholtz-Kohlrausch-effect
"""
from __future__ import annotations
import math
from .cam16 import (
    M16,
    M16_INV,
    M1,
    adapt,
    unadapt,
    hue_quadrature,
    inv_hue_quadrature
)
from .cam16 import Environment as _Environment
from .lch import LCh
from .. import util
from .. import algebra as alg
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from ..types import Vector, VectorLike


def hue_angle_dependency(h: float) -> float:
    """Calculate the hue angle dependency for CAM16."""
    pass


def eccentricity(h: float) -> float:
    """Calculate eccentricity."""
    pass


class Environment(_Environment):
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

    `hk`: Whether to adjust lightness for the Helmholtz-Kohlrausch effect.
    """

    def __init__(
        self,
        *,
        white: VectorLike,
        adapting_luminance: float,
        background_luminance: float,
        surround: str,
        discounting: bool,
        hk: bool,
    ) -> None:
        """
        Initialize environmental viewing conditions.

        Using the specified viewing conditions, and general environmental data,
        initialize anything that we can ahead of time to speed up the process.
        """
        pass

    def calculate_adaptation(self, xyz_w: Vector) -> None:
        """Calculate the adaptation of the reference point and related variables."""
        pass


def cam_to_xyz(
    J: float | None = None,
    C: float | None = None,
    h: float | None = None,
    s: float | None = None,
    Q: float | None = None,
    M: float | None = None,
    H: float | None = None,
    env: Environment | None = None
) -> Vector:
    """
    From CAM16 to XYZ.

    Reverse calculation can actually be obtained from a small subset of the CAM16 components
    Really, only one suitable value is needed for each type of attribute: (lightness/brightness),
    (chroma/colorfulness/saturation), (hue/hue quadrature). If more than one for a given
    category is given, we will fail as we have no idea which is the right one to use. Also,
    if none are given, we must fail as well as there is nothing to calculate with.
    """
    pass


def xyz_to_cam(xyz: Vector, env: Environment, calc_hue_quadrature: bool = False) -> Vector:
    """From XYZ to CAM16."""
    pass


def xyz_to_cam_jmh(xyz: Vector, env: Environment) -> Vector:
    """XYZ to CAM16 JMh with corrections."""
    pass


def cam_jmh_to_xyz(jmh: Vector, env: Environment) -> Vector:
    """CAM16 JMh with corrections to XYZ."""
    pass


class HellwigJMh(LCh):
    """CAM16 class (JMh) with corrections."""

    BASE = "xyz-d65"
    NAME = "hellwig-jmh"
    SERIALIZE = ("--hellwig-jmh",)
    CHANNEL_ALIASES = {
        "lightness": "j",
        "colorfulness": 'm',
        "hue": 'h'
    }
    WHITE = WHITES['2deg']['D65']
    HK = False

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
        discounting=False,
        # Account for Helmholtz-Kohlrausch effect
        hk=False
    )
    CHANNELS = (
        Channel("j", 0.0, 100.0),
        Channel("m", 0, 70.0),
        Channel("h", flags=FLG_ANGLE)
    )

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def radial_name(self) -> str:
        """Get radial name."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """Normalize."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """From CAM16 JMh to XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to CAM16 JMh."""
        pass


class HellwigHKJMh(HellwigJMh):
    """CAM16 class (JMh) with corrections and accounting for the Helmholtz-Kohlrausch effect."""

    NAME = "hellwig-hk-jmh"
    SERIALIZE = ("--hellwig-hk-jmh",)
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
        discounting=False,
        # Account for Helmholtz-Kohlrausch effect
        hk=True
    )
    CHANNELS = (
        Channel("j", 0.0, 101.56018891418564),
        Channel("m", 0, 70.0),
        Channel("h", flags=FLG_ANGLE)
    )
