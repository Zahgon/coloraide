"""
Delta E CAM16.

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9698626/pdf/sensors-22-08869.pdf
"""
from __future__ import annotations
import math
from . import DeltaE
from ..spaces.cam16_ucs import COEFFICENTS, CAM16UCS
from ..types import AnyColor
from typing import Any


class DECAM16(DeltaE):
    """Delta E CAM16 class."""

    NAME = "cam16"

    def distance(
        self,
        color: AnyColor,
        sample: AnyColor,
        space: str = "cam16-ucs",
        **kwargs: Any
    ) -> float:
        """Delta E CAM16 color distance formula."""
        pass
