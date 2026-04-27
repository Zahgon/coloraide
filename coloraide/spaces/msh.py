"""
Msh color space.

Accounts for negative lightness and uses degrees for hue instead of radians.

- https://www.kennethmoreland.com/color-maps/ColorMapsExpanded.pdf
"""
from __future__ import annotations
import math
from .lch import LCh
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE, ANGLE_RAD
from ..css import serialize
from ..types import Vector
from typing import TYPE_CHECKING, Sequence, Any

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color


def lab_to_msh(lab: Vector) -> Vector:
    """Convert CIE LCh to Msh."""
    pass


def msh_to_lab(msh: Vector) -> Vector:
    """Convert Msh to CIE Lab."""
    pass


class Msh(LCh):
    """Msh color space."""

    BASE = "lab-d65"
    NAME = "msh"
    SERIALIZE = ("--msh",)
    CHANNELS = (
        Channel("m", 0.0, 179.94996634797567),
        Channel("s", 0.0, 1.6),
        Channel("h", flags=FLG_ANGLE, angle=ANGLE_RAD)
    )
    CHANNEL_ALIASES = {
        "magnitude": "m",
        "saturation": "s",
        "hue": "h"
    }
    WHITE = WHITES['2deg']['D65']

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def lightness_name(self) -> str:
        """Get lightness name."""
        pass

    def radial_name(self) -> str:
        """Get radial name."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To Lab from LCh."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From Lab to LCh."""
        pass

    def to_string(
        self,
        parent: Color,
        *,
        alpha: bool | None = None,
        precision: int | Sequence[int] | None = None,
        rounding: str | None = None,
        fit: str | bool | dict[str, Any] = True,
        none: bool = False,
        percent: bool | Sequence[bool] = False,
        angle: str = 'rad',
        **kwargs: Any
    ) -> str:
        """Convert to CSS 'color' string: `color(space coords+ / alpha)`."""
        pass
