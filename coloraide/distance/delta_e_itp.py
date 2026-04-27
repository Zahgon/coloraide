"""
Delta E ITP.

https://kb.portrait.com/help/ictcp-color-difference-metric
"""
from __future__ import annotations
import math
from . import DeltaE
from ..types import AnyColor
from typing import Any


class DEITP(DeltaE):
    """Delta E ITP class."""

    NAME = "itp"

    def __init__(self, scalar: float = 720) -> None:
        """Initialize."""
        pass

    def distance(self, color: AnyColor, sample: AnyColor, scalar: float | None = None, **kwargs: Any) -> float:
        """Delta E ITP color distance formula."""
        pass
