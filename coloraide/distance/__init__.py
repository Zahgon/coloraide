"""Distance and Delta E."""
from __future__ import annotations
import math
from .. import algebra as alg
from abc import ABCMeta, abstractmethod
from ..types import ColorInput, Plugin, AnyColor
from typing import Any, Sequence


def closest(color: AnyColor, colors: Sequence[ColorInput], method: str | None = None, **kwargs: Any) -> AnyColor:
    """Get the closest color."""
    pass


def distance_euclidean(color: AnyColor, sample: AnyColor, space: str = "lab-d65") -> float:
    """
    Euclidean distance.

    https://en.wikipedia.org/wiki/Euclidean_distance
    """
    pass


class DeltaE(Plugin, metaclass=ABCMeta):
    """Delta E plugin class."""

    NAME = ''

    @abstractmethod
    def distance(self, color: AnyColor, sample: AnyColor, **kwargs: Any) -> float:
        """Get distance between color and sample."""
