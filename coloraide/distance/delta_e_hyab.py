"""HyAB distance."""
from __future__ import annotations
from . import DeltaE
import math
from ..spaces import Labish
from ..types import AnyColor
from typing import Any


class DEHyAB(DeltaE):
    """Delta E HyAB class."""

    NAME = "hyab"

    def __init__(self, space: str = "lab-d65") -> None:
        """Initialize."""
        pass

    def distance(self, color: AnyColor, sample: AnyColor, space: str | None = None, **kwargs: Any) -> float:
        """
        HyAB distance for Lab-ish spaces.

        http://markfairchild.org/PDFs/PAP40.pdf.
        """
        pass
