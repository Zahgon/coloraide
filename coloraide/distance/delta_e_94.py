"""Delta E 94."""
from __future__ import annotations
import math
from . import DeltaE
from ..spaces.lab import CIELab
from .. types import AnyColor
from typing import Any


class DE94(DeltaE):
    """Delta E 94 class."""

    NAME = "94"

    def __init__(
        self,
        kl: float = 1,
        k1: float = 0.045,
        k2: float = 0.015,
        space: str = 'lab-d65'
    ):
        """Initialize."""
        pass

    def distance(
        self,
        color: AnyColor,
        sample: AnyColor,
        kl: float | None = None,
        k1: float | None = None,
        k2: float | None = None,
        space: str | None = None,
        **kwargs: Any
    ) -> float:
        """
        Delta E 1994 color distance formula.

        http://www.brucelindbloom.com/Eqn_DeltaE_CIE94.html
        """
        pass
