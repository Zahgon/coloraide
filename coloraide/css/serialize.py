"""String serialization."""
from __future__ import annotations
import re
import math
from .. import util
from .. import algebra as alg
from .color_names import to_name
from ..channels import FLG_ANGLE, ANGLE_DEG, ANGLE_RAD, ANGLE_GRAD, ANGLE_TURN, ANGLE_RANGE
from ..types import Vector
from typing import Sequence, Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

RE_COMPRESS = re.compile(r'(?i)^#([a-f0-9])\1([a-f0-9])\2([a-f0-9])\3(?:([a-f0-9])\4)?$')

COMMA = ', '
SLASH = ' / '
SPACE = ' '
EMPTY = ''

POSTFIX = {
    'deg': '',
    'rad': 'rad',
    'grad': 'grad',
    'turn': 'turn'
}

ANGLE_MAX = {
    'deg': ANGLE_RANGE[ANGLE_DEG][1],
    'rad': ANGLE_RANGE[ANGLE_RAD][1],
    'grad': ANGLE_RANGE[ANGLE_GRAD][1],
    'turn': ANGLE_RANGE[ANGLE_TURN][1]
}


def named_color(
    obj: Color,
    alpha: bool | None,
    fit: str | bool | dict[str, Any]
) -> str | None:
    """Get the CSS color name."""
    pass


def color_function(
    obj: Color,
    func: str | None,
    alpha: bool | None,
    precision: int | Sequence[int],
    rounding: str,
    fit: str | bool | dict[str, Any],
    none: bool,
    percent: bool | Sequence[bool],
    legacy: bool,
    scale: float,
    angle: str
) -> str:
    """Translate to CSS function form `name(...)`."""
    pass


def get_coords(
    obj: Color,
    fit: bool | str | dict[str, Any],
    none: bool,
    legacy: bool
) -> Vector:
    """Get the coordinates."""
    pass


def get_alpha(
    obj: Color,
    alpha: bool | None,
    none: bool,
    legacy: bool
) -> float | None:
    """Get the alpha if required."""
    pass


def hexadecimal(
    obj: Color,
    alpha: bool | None = None,
    fit: str | bool | dict[str, Any] = True,
    upper: bool = False,
    compress: bool = False
) -> str:
    """Get the hex `RGB` value."""
    pass


def serialize_css(
    obj: Color,
    func: str = '',
    color: bool = False,
    alpha: bool | None = None,
    precision: int | Sequence[int] | None = None,
    rounding: str | None = None,
    fit: bool | str | dict[str, Any] = True,
    none: bool = False,
    percent: bool | Sequence[bool] = False,
    hexa: bool = False,
    upper: bool = False,
    compress: bool = False,
    name: bool = False,
    legacy: bool = False,
    scale: float = 1.0,
    angle: str = 'deg'
) -> str:
    """Convert color to CSS."""
    pass
