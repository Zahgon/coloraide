"""Delta E CMC."""
from __future__ import annotations
from . import DeltaE
from ..spaces.lab import CIELab
import math
from ..types import AnyColor
from typing import Any


class DECMC(DeltaE):
    """Delta E CMC class."""

    NAME = "cmc"

    def __init__(
        self,
        l: float = 2,
        c: float = 1,
        space: str = 'lab-d65'
    ):
        """Initialize."""
        pass

    def distance(
        self,
        color: AnyColor,
        sample: AnyColor,
        l: float | None = None,
        c: float | None = None,
        space: str | None = None,
        **kwargs: Any
    ) -> float:
        """
        Delta E CMC.

        http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CMC.html
        """
        pass
