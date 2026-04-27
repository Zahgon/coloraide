"""
Interpolation methods.

Originally, the base code for `interpolate`, `mix` and `steps` was ported from the
https://colorjs.io project. Since that time, there has been significant modifications
that add additional features etc. The base logic though is attributed to the original
authors.

In general, the logic mimics in many ways the `color-mix` function as outlined in the Level 5
color draft (Oct 2020), but the initial approach was modeled directly off of the work done in
color.js.
---
Original Authors: Lea Verou, Chris Lilley
License: MIT (As noted in https://github.com/LeaVerou/color.js/blob/master/package.json)
"""
from __future__ import annotations
import math
import bisect
import functools
import itertools as it
from abc import ABCMeta, abstractmethod
from .. import util
from .. import algebra as alg
from .. spaces import HSVish, HSLish, RGBish, LChish, Labish, HWBish
from ..types import Matrix, Vector, ColorInput, Plugin, AnyColor
from typing import Callable, Sequence, Mapping, Any, Generic, Iterable, TYPE_CHECKING

if TYPE_CHECKING:  #pragma: no cover
    from ..color import Color

__all__ = ('stop', 'hint', 'interpolator', 'Interpolate', 'Interpolator')


class Sentinel(float):
    """Sentinel object that is specific to averaging that we shouldn't see defined anywhere else."""


class stop:
    """Color stop."""

    __slots__ = ('color', 'stop')

    def __init__(self, color: ColorInput, value: float) -> None:
        """Color stops."""
        pass


def normalize_hue(
    h1: float,
    h2: float,
    hue: str,
    max_hue: float
) -> tuple[float, float]:
    """
    Adjust hues.

    Undefined hues are not resolved at this point in time.
    When interpolating between achromatic colors, hue specifications
    such as shorter and longer will have no affect as undefined hues
    will remain undefined meaning there is no arc length to choose
    between. This gives more intuitive interpolation results.
    """
    pass


def multi_mix(
    color_cls: type[AnyColor],
    colors: Iterable[ColorInput],
    weights: Iterable[float] | None,
    space: str,
    premultiplied: bool = True,
    carryforward: bool = False,
    powerless: bool = False,
    hue: str = 'shorter',
    average: bool = False
) -> AnyColor:
    """Mix multiple colors."""
    pass


def midpoint(t: float, h: float = 0.5) -> float:
    """Midpoint easing function."""
    pass


def hint(mid: float) -> Callable[..., float]:
    """A generate a midpoint easing function."""
    pass


def normalize_domain(d: Vector) -> Vector:
    """Normalize domain between 0 and 1."""
    pass


class Interpolator(Generic[AnyColor], metaclass=ABCMeta):
    """Interpolator."""

    def __init__(
        self,
        coordinates: Matrix,
        channel_names: Sequence[str],
        color_cls: type[AnyColor],
        easings: list[Callable[..., float] | None],
        stops: dict[int, float],
        space: str,
        out_space: str,
        progress: Mapping[str, Callable[..., float]] | Callable[..., float] | None,
        premultiplied: bool,
        extrapolate: bool = False,
        domain: Sequence[float] | None = None,
        padding: float | tuple[float, float] | None = None,
        hue: str = 'shorter',
        **kwargs: Any
    ):
        """Initialize."""
        pass

    def discretize(
        self,
        steps: int = 2,
        max_steps: int = 1000,
        max_delta_e: float = 0,
        delta_e: str | None = None,
        delta_e_args: dict[str, Any] | None = None,
    ) -> Interpolator[AnyColor]:
        """Make the interpolation a discretized interpolation."""
        pass

    def out_space(self, space: str) -> None:
        """Set output space."""
        pass

    def domain(self, domain: Sequence[float]) -> None:
        """Set the domain."""
        pass

    def padding(self, padding: float | Sequence[float]) -> None:
        """Add/adjust padding."""
        pass

    @abstractmethod
    def setup(self) -> None:
        """Setup."""

    @abstractmethod
    def interpolate(
        self,
        point: float,
        index: int,
    ) -> Vector:
        """Interpolate."""

    def steps(
        self,
        steps: int = 2,
        max_steps: int = 1000,
        max_delta_e: float = 0,
        delta_e: str | None = None,
        delta_e_args: dict[str, Any] | None = None,
    ) -> list[AnyColor]:
        """Steps."""
        pass

    def premultiply(self, coords: Vector, alpha: float | None = None) -> None:
        """Apply premultiplication to semi-transparent colors."""
        pass

    def postdivide(self, coords: Vector) -> None:
        """Undo premultiplication of semi-transparent colors."""
        pass

    def begin(self, point: float, first: float, last: float, index: int) -> AnyColor:
        """
        Begin interpolation.

        - Ensure point is relative to the stops.
        - Get the appropriate easing function.
        - Call interpolation.
        - Return a color
        """
        pass

    def ease(self, t: float, channel_index: int) -> float:
        """Provide a progression time and channel index."""
        pass

    def handle_domain(self, p: float) -> float:
        """
        Scale a point from a custom domain into a domain of 0 to 1.

        This allows a user to have a custom domain, but for us to adapt back to 0 and 1
        so that our logic can remain consistent.
        """
        pass

    def __call__(self, point: float) -> AnyColor:
        """Find which leg of the interpolation the request is between."""
        pass


class Interpolate(Plugin, metaclass=ABCMeta):
    """Interpolation plugin."""

    NAME = ""

    @abstractmethod
    def interpolator(
        self,
        coordinates: Matrix,
        channel_names: Sequence[str],
        color_cls: type[AnyColor],
        easings: list[Callable[..., float] | None],
        stops: dict[int, float],
        space: str,
        out_space: str,
        progress: Mapping[str, Callable[..., float]] | Callable[..., float] | None,
        premultiplied: bool,
        extrapolate: bool = False,
        domain: Vector | None = None,
        padding: float | tuple[float, float] | None = None,
        hue: str = 'shorter',
        **kwargs: Any
    ) -> Interpolator[AnyColor]:
        """Get the interpolator object."""

    def get_space(self, space: str | None, color_cls: type[AnyColor]) -> str:
        """
        Get and validate the color space for interpolation.

        If no space is defined, return an appropriate default color space.
        """
        pass

    def weighted_mix(
        self,
        color_cls: type[AnyColor],
        colors: Iterable[ColorInput],
        weights: Iterable[float] | None,
        space: str | None,
        premultiplied: bool = True,
        carryforward: bool = False,
        powerless: bool = False,
        hue: str = 'shorter',
        **kwargs: Any
    ) -> AnyColor:
        """Mix a list of colors together with weights."""
        pass


def calc_stops(stops: dict[int, float], count: int) -> dict[int, float]:
    """Calculate stops."""
    pass


def process_mapping(
    progress: Mapping[str, Callable[..., float]] | Callable[..., float] | None,
    aliases: Mapping[str, str]
) -> Mapping[str, Callable[..., float]] | Callable[..., float] | None:
    """Process a mapping, such that it is not using aliases."""
    pass


def carryforward_convert(color: Color, space: str, hue_index: int, powerless: bool) -> None:  # pragma: no cover
    """Carry forward undefined values during conversion."""
    pass


def weighted_mix(
    color_cls: type[AnyColor],
    interpolator: str,
    colors: Iterable[ColorInput],
    weights: Iterable[float] | None,
    space: str | None,
    premultiplied: bool = True,
    carryforward: bool = False,
    powerless: bool = False,
    hue: str = 'shorter',
    **kwargs: Any
) -> AnyColor:
    """Perform a weighted mix between multiple colors."""
    pass


def interpolator(
    color_cls: type[AnyColor],
    interpolator: str,
    colors: Sequence[ColorInput | stop | Callable[..., float]],
    space: str | None,
    out_space: str | None,
    progress: Mapping[str, Callable[..., float]] | Callable[..., float] | None,
    hue: str,
    premultiplied: bool,
    extrapolate: bool,
    domain: Vector | None = None,
    padding: float | tuple[float, float] | None = None,
    carryforward: bool = False,
    powerless: bool = False,
    **kwargs: Any
) -> Interpolator[AnyColor]:
    """Get desired blend mode."""
    pass
