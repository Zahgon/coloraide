"""Contrast."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from ..types import Plugin, AnyColor
from typing import Any


class ColorContrast(Plugin, metaclass=ABCMeta):
    """Color contrast plugin class."""

    NAME = ''

    @abstractmethod
    def contrast(self, color1: AnyColor, color2: AnyColor, **kwargs: Any) -> float:
        """Get the contrast of the two provided colors."""


def contrast(name: str | None, color1: AnyColor, color2: AnyColor, **kwargs: Any) -> float:
    """Get the appropriate contrast plugin."""
    pass
