"""Temperature plugin."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from ..types import Plugin, Vector, AnyColor
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color


class CCT(Plugin, metaclass=ABCMeta):
    """Delta E plugin class."""

    NAME = ''

    @abstractmethod
    def to_cct(self, color: Color, **kwargs: Any) -> Vector:
        """Calculate a color's CCT."""

    @abstractmethod
    def from_cct(
        self,
        kelvin: float,
        duv: float,
        **kwargs: Any
    ) -> tuple[tuple[float, float], str]:
        """Calculate a color that satisfies the CCT."""


def cct(name: str | None, color: type[AnyColor] | AnyColor) -> CCT:
    """Get the appropriate contrast plugin."""
    pass
