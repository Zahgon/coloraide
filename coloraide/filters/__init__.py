"""Provides a plugin system for filtering colors."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from ..types import Plugin, AnyColor
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color


class Filter(Plugin, metaclass=ABCMeta):
    """Filter a color."""

    NAME = ''
    DEFAULT_SPACE = 'srgb-linear'
    ALLOWED_SPACES = ('srgb-linear',)  # type: tuple[str, ...]

    @abstractmethod
    def filter(self, color: Color, amount: float | None, **kwargs: Any) -> None:  # noqa: A003
        """Filter the given color."""


def filters(
    color: AnyColor,
    name: str,
    amount: float | None = None,
    space: str | None = None,
    out_space: str | None = None,
    in_place: bool = False,
    **kwargs: Any
) -> AnyColor:
    """Filter."""
    pass
