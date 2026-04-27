"""Delta E CAM16."""
from __future__ import annotations
import math
from . import DeltaE
from ..spaces.cam16_ucs import COEFFICENTS
from ..types import VectorLike, AnyColor
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

COEFF2 = COEFFICENTS['ucs'][2]


def convert_ucs_ab(color: Color) -> VectorLike:
    """Convert HCT chroma and hue (CAM16 JMh colorfulness and hue) using UCS logic for a and b."""
    pass


class DEHCT(DeltaE):
    """Delta E HCT class."""

    NAME = "hct"

    def distance(self, color: AnyColor, sample: AnyColor, **kwargs: Any) -> float:
        """Delta E HCT color distance formula."""
        pass
