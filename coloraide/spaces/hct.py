"""
HCT color space.

This implements the HCT color space as described. This is not a port of the Material library.
We simply, as described, create a color space with CIELAB L* and CAM16's C and h components.
Environment settings are calculated with the assumption of L* 50.

Generally, the HCT color space is restricted to sRGB and SDR range in the Material library, but we do
not have such restrictions.

Though we did not port HCT from Material Color Utilities, we did test against it, and are pretty
much on point. The only differences are due to matrix precision and white point precision. Material
uses an RGB <-> XYZ matrix that rounds values off significantly more than we do. Also, while we
calculate the XYZ points from the `xy` points without rounding, they have rounded XYZ points. Lastly,
the gamut mapping algorithm we use is likely different even though it arrives at pretty much the same
result, so slightly different values can occur.

Material:

```
> hct.Hct.fromInt(0xff305077)
Hct {
  argb: 4281356407,
  internalHue: 256.8040416857594,
  internalChroma: 31.761442797741243,
  internalTone: 33.34501410942328
}
```

ColorAide:

```
>>> from coloraide_extras.everything import ColorAll as Color
>>> Color('#305077').convert('hct')
color(--hct 256.79 31.766 33.344 / 1)
```

"""
from __future__ import annotations
from .. import algebra as alg
from .lch import LCh
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
from .cam16 import Environment, cam_to_xyz, xyz_to_cam
from .lab import y_to_lstar, lstar_to_y
from ..types import Vector
import math


def hct_to_xyz(coords: Vector, env: Environment) -> Vector:
    """
    Convert HCT to XYZ.

    Use Newton's method to try and converge as quick as possible or converge as
    close as we can. While the requested precision is achieved most of the time,
    it may not always be achievable. Especially past the visible spectrum, the
    algorithm will likely struggle to get the same precision. If, for whatever
    reason, we cannot achieve the accuracy we seek in the allotted iterations,
    just return the closest we were able to get.
    """
    pass


def xyz_to_hct(coords: Vector, env: Environment) -> Vector:
    """Convert XYZ to HCT."""
    pass


class HCT(LCh):
    """HCT class."""

    BASE = "xyz-d65"
    NAME = "hct"
    SERIALIZE = ("--hct",)
    WHITE = WHITES['2deg']['D65']
    ENV = Environment(
        # D65 white point.
        white=WHITE,
        # 200 lux or `~11.72 cd/m2` multiplied by ~18.42%, a variation of gray world assumption.
        adapting_luminance=200 / math.pi * lstar_to_y(50.0),
        # A variation on gray world assumption: ~18.42% of reference white's `Yw == 100`.
        background_luminance=lstar_to_y(50.0) * 100,
        # Average surround.
        surround='average',
        # No discounting of illuminant.
        discounting=False
    )
    CHANNEL_ALIASES = {
        "lightness": "t",
        "tone": "t",
        "chroma": "c",
        "hue": "h"
    }

    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("c", 0.0, 145.0),
        Channel("t", 0.0, 100.0)
    )

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """Normalize."""
        pass

    def names(self) -> tuple[Channel, ...]:
        """Return LCh-ish names in the order L C h."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To XYZ from CAM16."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From XYZ to CAM16."""
        pass
