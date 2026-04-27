"""Fit by compressing chroma in LCh."""
from __future__ import annotations
import functools
from . import Fit, clip_channels
from ..cat import WHITES
from .. import util
import math
from .. import algebra as alg
from .tools import adaptive_hue_independent
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

XYZ = 'xyz-d65'
try:
    WHITE = util.xy_to_xyz(WHITES['2deg']['D65'])
except (NotImplementedError, TypeError, AttributeError):
    WHITE = (0.0, 0.0, 0.0)
BLACK = [0.0, 0.0, 0.0]


@functools.lru_cache(maxsize=10)
def calc_epsilon(jnd: float) -> float:
    """Calculate the epsilon to 2 degrees smaller than the specified JND."""
    pass


class MINDEChroma(Fit):
    """
    Chroma reduction with MINDE.

    Adjust chroma (using binary search) which helps preserve perceptual hue and lightness.
    Compress chroma until we are right at the JND edge while still out of gamut.
    Raise the lower chroma bound while we are in gamut or outside of gamut but still under the JND.
    Lower the upper chroma bound anytime we are out of gamut and above the JND.
    Too far under the JND we'll reduce chroma too aggressively.

    This is the same as the CSS algorithm as described here: https://www.w3.org/TR/css-color-4/#binsearch.
    There are some small adjustments to handle HDR colors as the CSS algorithm assumes SDR color spaces.
    Additionally, this uses LCh instead of OkLCh, but we also offer a derived version that uses OkLCh.
    """

    NAME = "minde-chroma"
    JND = 0.02
    DE_OPTIONS = {"method": "ok"}  # type: dict[str, Any]
    PSPACE = "oklch"
    MIN_CONVERGENCE = 0.0001

    def fit(
        self,
        color: Color,
        space: str,
        *,
        pspace: str | None = None,
        jnd: float | None = None,
        de_options: dict[str, Any] | None = None,
        adaptive: float = 0.0,
        **kwargs: Any
    ) -> None:
        """Gamut mapping via CIELCh chroma."""
        pass
