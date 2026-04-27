"""
Easing functions.

https://drafts.csswg.org/css-easing/#easing-functions
https://probablymarcus.com/blocks/2015/02/26/using-bezier-curves-as-easing-functions.html
https://en.wikipedia.org/wiki/Horner%27s_method
https://en.wikipedia.org/wiki/Newton%27s_method

Since we know that control points P0 and P3 are always (0, 0) and (1, 1) respectively,
we can simplify the Bezier algorithm to:

```
x(t) = x0(1 - t)3 + 3x1(1 - t)2t + 3x2(1 - t)t2 + x3t3
x'(t) = 3(1 - t)2(x1 - x0) + 6(1 - t)t(x2 - x1) + 3t2(x3 - x2)
```

Further, they can be simplified to (Horner's method).

```
x(t) = (((1 - 3x2 + 3x1)t + 3x2 - 6x1)t + 3x1)t
x'(t) = 3(1 - 3x2 + 3x1)t2 + 2(3x2 - 6x1)t + 3x1
```

This allows us to calculate coefficients:

```
cx = 3.0 * p1x;
bx = 3.0 * (p2x - p1x) - cx;
ax = 1.0 - cx - bx;
```

And end up with:

```
x(t) = axt3 + bxt2 + cxt
x'(t) = 3axt2 + 2bxt + cx
```

This greatly simplifies things and makes it faster.
"""
from __future__ import annotations
import functools
from . import algebra as alg
from typing import Callable


def _bezier(a: float, b: float, c: float, y: float = 0.0) -> Callable[[float], float]:
    """
    Calculate the Bezier point.

    We know that P0 and P3 are always (0, 0) and (1, 1) respectively.
    Knowing this we can simplify the equation by precalculating them in.
    """
    pass


def _solve_bezier(
    target: float,
    a: float,
    b: float,
    c: float
) -> float:
    """
    Solve curve to find a `t` that satisfies our desired `x` (target).

    The `target` is expected to be within the range of 0 - 1, this will yield a `t` within that same range.
    """
    pass


def _extrapolate(t: float, p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """
    Extrapolate.

    Try to use the closest tangent to the endpoint, but if we can't,
    we'll just end up returning the same `t`.
    """
    pass


def _calc_bezier(
    target: float,
    a: tuple[float, float],
    b: tuple[float, float],
    c: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float]
) -> float:
    """
    Calculate the y value of the bezier curve with the given `x`.

    The value given is actually the target `x`. We need to find a
    `t` that satisfies the `x` so that we can find the `y`.
    """
    pass


def cubic_bezier(x1: float, y1: float, x2: float, y2: float) -> Callable[..., float]:
    """Return a cubic bezier easing function."""
    pass


def linear(t: float) -> float:
    """Linear."""
    pass


# CSS Easings Level 2
try:
    ease = cubic_bezier(0.25, 0.1, 0.25, 1.0)
except (NotImplementedError, TypeError, AttributeError):
    ease = None
try:
    ease_in = cubic_bezier(0.42, 0.0, 1.0, 1.0)
except (NotImplementedError, TypeError, AttributeError):
    ease_in = None
try:
    ease_out = cubic_bezier(0.0, 0.0, 0.58, 1.0)
except (NotImplementedError, TypeError, AttributeError):
    ease_out = None
try:
    ease_in_out = cubic_bezier(0.42, 0.0, 0.58, 1.0)
except (NotImplementedError, TypeError, AttributeError):
    ease_in_out = None
