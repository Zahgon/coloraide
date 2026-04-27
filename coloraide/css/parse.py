"""Parse utilities."""
from __future__ import annotations
import re
import math
from .. import algebra as alg
from ..types import Vector
from . import color_names
from ..channels import Channel, FLG_ANGLE, ANGLE_DEG
from typing import TYPE_CHECKING, Any
import functools

if TYPE_CHECKING:  # pragma: no cover
    from ..spaces import Space

RGB_CHANNEL_SCALE = 1.0 / 255.0
SCALE_PERCENT = 1 / 100.0
MAX_CHANNELS = 16

CONVERT_TURN = 360
CONVERT_GRAD = 90 / 100
CONVERT_RAD = 180 / math.pi

RE_HEX = re.compile(r'(?i)(\#)((?:[a-f0-9]{6}(?:[a-f0-9]{2})?|[a-f0-9]{3}(?:[a-f0-9])?))\b')
RE_NAME = re.compile(r'(?i)\b([a-z]{3,})\b')
RE_IDENT = re.compile(r'(?i)(-{0,2}[a-z][-a-z0-9_]*)')
RE_SPACE = re.compile(r'(\s+)')
RE_LOOSE_SPACE = re.compile(r'(\s*)')
RE_CHANNEL = re.compile(r'(?i)((?:[+\-]?(?:[0-9]*\.)?[0-9]+(?:e[-+]?[0-9]+)?))(?:(%)|(deg|rad|turn|grad))?|(none)')
RE_FUNC_START = re.compile(r'(\()\s*')
RE_FUNC_END = re.compile(r'\s*(\))')
RE_COMMA = re.compile(r'\s*(,)\s*')
RE_SLASH = re.compile(r'\s*(/)\s*')
RE_CSS_FUNC = re.compile(r'\b(color|rgba?|hsla?|hwb|(?:ok)?lab|(?:ok)?lch|jzazbz|jzczhz|ictcp)\b')


def norm_float(string: str) -> float:
    """Normalize a float value."""
    pass


def norm_hex_channel(string: str) -> float:
    """Normalize the hex string to a form we can handle."""
    pass


def norm_percent_channel(string: str, scale: float = 100, offset: float = 0.0) -> float:
    """Normalize percent channel."""
    pass


def norm_color_channel(string: str, scale: float = 1, offset: float = 0.0) -> float:
    """Normalize percent/number channel."""
    pass


def norm_scaled_color_channel(string: str, scale: float = 1, offset: float = 0.0) -> float:
    """Normalize scaled percent/number channel."""
    pass


def norm_rgb_channel(string: str, scale: float = 1) -> float:
    """Normalize RGB channel."""
    pass


def norm_alpha_channel(string: str) -> float:
    """Normalize alpha channel."""
    pass


def norm_angle_channel(angle: str) -> float:
    """Normalize angle units."""
    pass


def parse_hex(color: str) -> tuple[Vector, float]:
    """Parse hexadecimal color."""
    pass


def parse_rgb_channels(color: list[str], boundry: tuple[Channel, ...]) -> tuple[Vector, float]:
    """Parse CSS RGB format."""
    pass


def parse_channels(color: list[str], boundry: tuple[Channel, ...], scaled: bool = False) -> tuple[Vector, float]:
    """Parse CSS channel format."""
    pass


def parse_color(tokens: dict[str, Any], space: Space) -> tuple[Vector, float] | None:
    """Parse the color function."""
    pass


def validate_color(tokens: dict[str, Any]) -> bool:
    """Validate the color function syntax."""
    pass


def validate_srgb(tokens: dict[str, Any]) -> bool:
    """Validate the RGB color functions."""
    pass


def validate_cylindrical_srgb(tokens: dict[str, Any]) -> bool:
    """Validate cylindrical sRGB."""
    pass


def validate_lab(tokens: dict[str, Any]) -> bool:
    """Validate CSS Lab variant color spaces."""
    pass


def validate_lch(tokens: dict[str, Any]) -> bool:
    """Validate CSS LCh variant color spaces."""
    pass


@functools.lru_cache(maxsize=1)
def tokenize_css(css: str, start: int = 0) -> dict[str, Any]:
    """Tokenize the CSS string."""
    pass


def parse_css(
    cspace: Space,
    string: str,
    start: int = 0,
    fullmatch: bool = True,
    color: bool = False
) -> tuple[tuple[Vector, float], int] | None:
    """Match a CSS color string."""
    pass
