"""Channels."""
from __future__ import annotations
import math
from typing import Callable
from . import algebra as alg

FLG_ANGLE = 1
FLG_PERCENT = 2
FLG_OPT_PERCENT = 4
FLG_MIRROR_PERCENT = 8
ANGLE_NULL = 0
ANGLE_DEG = 1
ANGLE_RAD = 2
ANGLE_GRAD = 3
ANGLE_TURN = 4

ANGLE_RANGE = {
    ANGLE_DEG: (0.0, 360.0),
    ANGLE_RAD: (0.0, math.tau),
    ANGLE_GRAD: (0.0, 400),
    ANGLE_TURN: (0.0, 1.0)
}


class Channel(str):
    """Channel."""

    low: float
    high: float
    span: float
    offset: float
    bound: bool
    flags: int
    limit: Callable[[float], float | int]
    nans: float
    angle: int

    def __new__(
        cls,
        name: str,
        low: float = 0.0,
        high: float = 1.0,
        bound: bool = False,
        flags: int = 0,
        limit: Callable[[float], float | int] | tuple[float | None, float | None] | None = None,
        nans: float = 0.0,
        angle: int = ANGLE_NULL
    ) -> Channel:
        """Initialize."""
        pass
