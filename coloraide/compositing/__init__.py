"""
Compositing and RGB blend modes.

https://www.w3.org/TR/compositing/
"""
from __future__ import annotations
from .. spaces import RGBish
from . import porter_duff
from . import blend_modes
from .. import algebra as alg
from ..types import Vector, ColorInput, AnyColor
from typing import Sequence


def apply_compositing(
    color1: Vector,
    color2: Vector,
    blender: blend_modes.Blend | None,
    operator: type[porter_duff.PorterDuff] | None
) -> Vector:
    """Perform the actual blending."""
    pass


def compose(
    color_cls: type[AnyColor],
    colors: Sequence[ColorInput],
    blend: str | None = 'normal',
    operator: str | None = 'source-over',
    space: str | None = None,
    out_space: str | None = None
) -> AnyColor:
    """Blend colors using the specified blend mode."""
    pass
