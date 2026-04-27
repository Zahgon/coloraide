"""
Cubehelix color space.

Dave Green's Cubehelix colour scheme adapted to a color space.
https://arxiv.org/pdf/1108.5083.pdf

The paper does not describe a color space, but a way to create various
helixes to generate various Cubehelix schemes. Mike Bostock and Jason Davies
adapted this to a color space in D3 Color (https://github.com/d3/d3-color). We
match the algorithm here as implemented in D3.

Copyright 2010-2022 Mike Bostock

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted, provided that the above copyright notice
and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
"""
from __future__ import annotations
from . hsl import HSL
from ..cat import WHITES
from ..channels import Channel, FLG_ANGLE
import math
from .. import util
from ..types import Vector

# Constants
A = -0.14861
B = 1.78277
C = -0.29227
D = -0.90649
E = 1.97294
ED = E * D
EB = E * B
BC_DA = B * C - D * A
MAX_SAT = 4.614386868039719


def srgb_to_cubehelix(coords: Vector) -> Vector:
    """Convert sRGB to Cubehelix."""
    pass


def cubehelix_to_srgb(coords: Vector) -> Vector:
    """Convert Cubehelix to sRGB."""
    pass


class Cubehelix(HSL):
    """Cubehelix class."""

    BASE = 'srgb'
    NAME = "cubehelix"
    SERIALIZE = ("--cubehelix",)
    CHANNELS = (
        Channel("h", flags=FLG_ANGLE),
        Channel("s", 0.0, MAX_SAT, bound=True),
        Channel("l", 0.0, 1.0, bound=True)
    )
    CHANNEL_ALIASES = {
        "hue": "h",
        "saturation": "s",
        "lightness": "l"
    }
    WHITE = WHITES['2deg']['D65']
    GAMUT_CHECK = 'srgb'

    def normalize(self, coords: Vector) -> Vector:
        """Normalize coordinates."""
        pass

    def is_achromatic(self, coords: Vector) -> bool:
        """Check if color is achromatic."""
        pass

    def to_base(self, coords: Vector) -> Vector:
        """To LChuv from HSLuv."""
        pass

    def from_base(self, coords: Vector) -> Vector:
        """From LChuv to HSLuv."""
        pass
