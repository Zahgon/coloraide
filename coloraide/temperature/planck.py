"""
Planckian curve.

https://en.wikipedia.org/wiki/Planckian_locus#The_Planckian_locus_in_the_XYZ_color_space
"""
from __future__ import annotations
import math
from ..types import VectorLike, Vector
from ..cmfs import CMFs
from .. import util

# Constants for Planck's Law
# Precise calculation
# ```
# H = 6.62607015e-34  # Plank's constant: `m2 kg / s`
# C = 299792458  # Speed of light: `m / s`
# K = 1.380649e-23  # Boltzmann constant: `m2 kg s-2 K-1`
# C1 = 2 * math.pi * H * C ** 2  # First radiation constant
# C2 = (H * C) / K  # Second radiation constant
# ```
# ITS-90 Standard rounds to 6 decimal places
C1 = 3.741771e-16
C2 = 1.4388e-2


def temp_to_xy_planckian_locus(
    temp: float,
    cmfs: CMFs,
    white: VectorLike,
    start: int = 360,
    end: int = 830,
    step: int = 5,
    c1: float = C1,
    c2: float = C2
) -> Vector:
    """
    Temperature to Planckian locus.

    https://en.wikipedia.org/wiki/Planckian_locus#The_Planckian_locus_in_the_XYZ_color_space
    """
    pass
