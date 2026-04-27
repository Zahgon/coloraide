"""
ZCAM.

```
- ZCAM: https://opg.optica.org/oe/fulltext.cfm?uri=oe-29-4-6036.
- Supplemental ZCAM (inverse transform): https://opticapublishing.figshare.com/articles/journal_contribution/\
  Supplementary_document_for_ZCAM_a_psychophysical_model_for_colour_appearance_prediction_-_5022171_pdf/13640927.
- Two-stage chromatic adaptation by Qiyan Zhai and Ming R. Luo using CAM02: https://opg.optica.org/oe/\
  fulltext.cfm?uri=oe-26-6-7724&id=383537
```
"""
from __future__ import annotations
import math
from .. import util
from .. import algebra as alg
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from ..types import Vector, VectorLike
from .lch import LCh
from .jzazbz import izazbz_to_xyz, xyz_to_izazbz
from .cam16 import hue_quadrature, inv_hue_quadrature
from .. import cat

try:
    DEF_ILLUMINANT_BI = util.xyz_to_absxyz(util.xy_to_xyz(cat.WHITES['2deg']['E']), yw=100.0)
except (NotImplementedError, TypeError, AttributeError):
    DEF_ILLUMINANT_BI = (0.0, 0.0, 0.0)
CAT02 = cat.CAT02.MATRIX
CAT02_INV = [
    [1.0961238208355142, -0.27886900021828726, 0.18274517938277304],
    [0.45436904197535916, 0.4735331543074118, 0.07209780371722913],
    [-0.009627608738429355, -0.00569803121611342, 1.0153256399545427]
]

# ZCAM uses a slightly different matrix than Jzazbz
# It updates how `Iz` is calculated.
LMS_P_TO_IZAZBZ = [
    [0.0, 1.0, 0.0],
    [3.524, -4.066708, 0.542708],
    [0.199076, 1.096799, -1.295875]
]
IZAZBZ_TO_LMS_P = [
    [1.0, 0.2772100865430786, 0.11609463231223774],
    [1.0, 0.0, 0.0],
    [1.0, 0.042585801245220344, -0.75384457989992]
]

SURROUND = {
    'dark': (0.8, 0.525, 0.8),
    'dim': (0.9, 0.59, 0.9),
    'average': (1, 0.69, 1)
}

HUE_QUADRATURE = {
    # Red, Yellow, Green, Blue, Red
    "h": (33.44, 89.29, 146.30, 238.36, 393.44),
    "e": (0.68, 0.64, 1.52, 0.77, 0.68),
    "H": (0.0, 100.0, 200.0, 300.0, 400.0)
}


def adapt(
    xyz_b: Vector,
    xyz_wb: Vector,
    xyz_wd: Vector,
    db: float,
    dd: float,
    xyz_wo: Vector = DEF_ILLUMINANT_BI
) -> Vector:
    """
    Use 2 step chromatic adaptation by Qiyan Zhai and Ming R. Luo using CAM02.

    https://opg.optica.org/oe/fulltext.cfm?uri=oe-26-6-7724&id=383537

    `xyz_b`: the sample color
    `xyz_wb`: input illuminant of the sample color
    `xyz_wd`: output illuminant
    `xyz_wo`: the baseline illuminant, by default we use equal energy.
    """
    pass


class Environment:
    """
    Class to calculate and contain any required environmental data (viewing conditions included).

    While originally for CIECAM models, the following applies to ZCAM as well.
    Usage Guidelines for CIECAM97s (Nathan Moroney)
    https://www.imaging.org/site/PDFS/Papers/2000/PICS-0-81/1611.pdf

    white: This is the (x, y) chromaticity points for the white point. ZCAM is designed to use D65.
        Generally, D65 should always be used, but we allow the possibility of variants of D65. This should
        be the same value as set in the color class `WHITE` value.

    ref_white: The reference white in XYZ scaled by 100.

    adapting_luminance: This is the luminance of the adapting field. The units are in cd/m2.
        The equation is `L = (E * R) / π`, where `E` is the illuminance in lux, `R` is the reflectance,
        and `L` is the luminance. If we assume a perfectly reflecting diffuser, `R` is assumed as 1.
        For the "gray world" assumption, we must also divide by 5 (or multiply by 0.2 - 20%).
        This results in `La = E / π * 0.2`. You can also ignore this gray world assumption converting
        lux directly to nits (cd/m2) `lux / π`.

    background_luminance: The background is the region immediately surrounding the stimulus and
        for images is the neighboring portion of the image. Generally, this value is set to a value of 20.
        This implicitly assumes a gray world assumption.

    surround: The surround is categorical and is defined based on the relationship between the relative
        luminance of the surround and the luminance of the scene or image white. While there are 4 defined
        surrounds, usually just `average`, `dim`, and `dark` are used.

        Dark    | 0%        | Viewing film projected in a dark room
        Dim     | 0% to 20% | Viewing television
        Average | > 20%     | Viewing surface colors

    discounting: Whether we are discounting the illuminance. Done when eye is assumed to be fully adapted.
    """

    def __init__(
        self,
        *,
        white: VectorLike,
        reference_white: VectorLike,
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


def zcam_to_xyz(
    Jz: float | None = None,
    Cz: float | None = None,
    hz: float | None = None,
    Qz: float | None = None,
    Mz: float | None = None,
    Sz: float | None = None,
    Vz: float | None = None,
    Kz: float | None = None,
    Wz: float | None = None,
    Hz: float | None = None,
    env: Environment | None = None
) -> Vector:
    """
    From ZCAM to XYZ.

    Reverse calculation can actually be obtained from a small subset of the ZCAM components
    Really, only one suitable value is needed for each type of attribute: (lightness/brightness),
    (chroma/colorfulness/saturation), (hue/hue quadrature). If more than one for a given
    category is given, we will fail as we have no idea which is the right one to use. Also,
    if none are given, we must fail as well as there is nothing to calculate with.
    """
    pass


def xyz_to_zcam(xyz: Vector, env: Environment, calc_hue_quadrature: bool = False) -> Vector:
    """From XYZ to ZCAM."""
    pass


def xyz_to_zcam_jmh(xyz: Vector, env: Environment) -> Vector:
    """XYZ to ZCAM JMh."""
    pass


def zcam_jmh_to_xyz(jmh: Vector, env: Environment) -> Vector:
    """ZCAM JMh to XYZ."""
    pass


class ZCAMJMh(LCh):
    """ZCAM class (JMh)."""

    BASE = "xyz-d65"
    NAME = "zcam-jmh"
    SERIALIZE = ("--zcam-jmh",)
    CHANNEL_ALIASES = {
        "lightness": "jz",
        "colorfulness": 'mz',
        "hue": 'hz',
        'j': 'jz',
        'm': "mz",
        'h': 'hz'
    }
    WHITE = WHITES['2deg']['D65']
    DYNAMIC_RANGE = 'hdr'
    ENV = Environment(
        # This must be a D65 white point, and will be scaled by 100 to be "absolute".
        white=WHITE,
        # The absolute XYZ reference white
        reference_white=util.xyz_to_absxyz(util.xy_to_xyz(WHITE), 100),
        # Assuming sRGB which has a lux of 64: `((E * R) / PI)` where `R = 1`.
        # Divided by 5 (or multiplied by 20%) assuming gray world.
        adapting_luminance=64 / math.pi * 0.2,
        # 20% relative to an XYZ luminance of 100 (scaled by 100) for the gray world assumption.
        background_luminance=20,
        # Assume an average surround
        surround='average',
        # Do not discount illuminant.
        discounting=False
    )
    CHANNELS = (
        Channel("jz", 0.0, 100.0),
        Channel("mz", 0.0, 60.0),
        Channel("hz", flags=FLG_ANGLE)
    )

    def normalize(self, coords: Vector) -> Vector:
        """Normalize."""
        pass

    def hue_name(self) -> str:
        """Hue name."""
        pass

    def radial_name(self) -> str:
        """Radial name."""
        pass

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """From ZCAM JMh to XYZ."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to ZCAM JMh."""
        pass
