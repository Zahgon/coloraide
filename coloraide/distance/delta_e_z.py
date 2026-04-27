"""
Delta E z.

https://www.osapublishing.org/oe/fulltext.cfm?uri=oe-25-13-15131&id=368272
"""
from __future__ import annotations
import math
from . import DeltaE
from ..types import AnyColor
from typing import Any


class DEZ(DeltaE):
    """Delta E z class."""

    NAME = "jz"

    def distance(self, color: AnyColor, sample: AnyColor, **kwargs: Any) -> float:
        """Delta E z color distance formula."""
        pass
