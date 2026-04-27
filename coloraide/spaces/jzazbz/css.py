"""Jzazbz class."""
from __future__ import annotations
from .. import jzazbz as base
from ...css import parse
from ...css import serialize
from ...types import Vector
from typing import Any, Sequence, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ...color import Color


class Jzazbz(base.Jzazbz):
    """Jzazbz class."""

    def to_string(
        self,
        parent: Color,
        *,
        alpha: bool | None = None,
        precision: int | Sequence[int] | None = None,
        rounding: str | None = None,
        fit: bool | str | dict[str, Any] = True,
        none: bool = False,
        color: bool = False,
        percent: bool | Sequence[bool] = False,
        **kwargs: Any
    ) -> str:
        """Convert to CSS."""
        pass

    def match(
        self,
        string: str,
        start: int = 0,
        fullmatch: bool = True
    ) -> tuple[tuple[Vector, float], int] | None:
        """Match a CSS color string."""
        pass
