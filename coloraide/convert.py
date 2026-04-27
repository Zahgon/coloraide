"""Convert the color."""
from __future__ import annotations
from .types import Vector
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from .spaces import Space
    from .color import Color

# XYZ is the absolute base, meaning that XYZ is the final base in any conversion chain.
# This is a design expectation regardless of whether someone assigns a different base to XYZ or not.
ABSOLUTE_BASE = 'xyz-d65'


def calc_path_to_xyz(
    color: type[Color],
    space: str
) -> tuple[list[Space], dict[str, int]]:
    """
    Calculate the conversion path between a given color space and XYZ D65.

    We create two structures:

    1. A list containing the color space name in the conversion process from our target to XYZ D65.
    2. A mapping of color space names to the index in the color space name list.
    """
    pass


def get_convert_chain(
    color: type[Color],
    space: Space,
    target: str
) -> list[tuple[Space, Space, int, bool]]:
    """
    Create a conversion chain.

    Each entry in the list will contain (from_space, to_space, direction, chromatic_adaptation_needed).
    Direction refers to whether conversions are moving to or from XYZ D65 as that will dictate whether
    `to_base` or `from_base` call method is used. If either the "from" or "to" color space is XYZ D65
    a chromatic adaptation will need to occur.
    """
    pass


def convert(color: Color, space: str) -> tuple[Space, Vector]:
    """Convert the color coordinates to the specified space."""
    pass
