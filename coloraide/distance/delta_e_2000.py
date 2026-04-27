"""Delta E 2000."""
from __future__ import annotations
import math
from . import DeltaE
from ..spaces.lab import CIELab
from ..types import AnyColor
from typing import Any


class DE2000(DeltaE):
    """Delta E 2000 class."""

    NAME = "2000"
    G_CONST = 25 ** 7

    def __init__(
        self,
        kl: float = 1,
        kc: float = 1,
        kh: float = 1,
        space: str = 'lab-d65'
    ):
        """Initialize."""
        pass

    def distance(
        self,
        color: AnyColor,
        sample: AnyColor,
        kl: float | None = None,
        kc: float | None = None,
        kh: float | None = None,
        space: str | None = None,
        **kwargs: Any
    ) -> float:
        """
        Calculate distance doing a direct translation of the algorithm from the CIE Delta E 2000 paper.

        We denoted prime (L') with trailing 'p' and mean is represented with a trailing 'm'.
        Delta has a preceding 'd'. I'm not sure I was completely consistent.

        http://www2.ece.rochester.edu/~gsharma/ciede2000/ciede2000noteCRNA.pdf
        """
        pass
