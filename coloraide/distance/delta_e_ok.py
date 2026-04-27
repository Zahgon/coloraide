"""Delta E OK."""
from __future__ import annotations
from . import DeltaE, distance_euclidean
from ..types import AnyColor
from typing import Any


class DEOK(DeltaE):
    """Delta E 99o class."""

    NAME = 'ok'

    def __init__(self, scalar: float = 1) -> None:
        """Initialize."""
        pass

    def distance(self, color: AnyColor, sample: AnyColor, scalar: float | None = None, **kwargs: Any) -> float:
        """
        Delta E OK color distance formula.

        This just uses simple Euclidean distance in the Oklab color space.
        """
        pass
