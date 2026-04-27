"""Colors."""

from __future__ import annotations
import sys
import abc
import functools
import random
import math
from contextlib import contextmanager
from . import cat
from . import distance
from . import convert
from . import gamut
from . import compositing
from . import interpolate
from . import filters
from . import contrast
from . import harmonies
from . import temperature
from . import util
from . import algebra as alg
from . import spectrum
from .channels import ANGLE_DEG, ANGLE_RAD, ANGLE_GRAD, ANGLE_TURN, ANGLE_NULL
from .deprecate import warn_deprecated, deprecated
from itertools import zip_longest as zipl
from .css import parse
from .types import VectorLike, Vector, ColorInput
from .spaces import Space
from .spaces.hsv import HSV
from .spaces.srgb.css import sRGB
from .spaces.srgb_linear import sRGBLinear
from .spaces.hsl.css import HSL
from .spaces.hwb.css import HWB
from .spaces.lab.css import Lab
from .spaces.lch.css import LCh
from .spaces.lab_d65 import LabD65
from .spaces.lch_d65 import LChD65
from .spaces.display_p3 import DisplayP3
from .spaces.display_p3_linear import DisplayP3Linear
from .spaces.a98_rgb import A98RGB
from .spaces.a98_rgb_linear import A98RGBLinear
from .spaces.prophoto_rgb import ProPhotoRGB
from .spaces.prophoto_rgb_linear import ProPhotoRGBLinear
from .spaces.rec2020 import Rec2020
from .spaces.rec2020_linear import Rec2020Linear
from .spaces.xyz_d65 import XYZD65
from .spaces.xyz_d50 import XYZD50
from .spaces.oklab.css import Oklab
from .spaces.oklch.css import OkLCh
from .spaces.rec2100_pq import Rec2100PQ
from .spaces.rec2100_hlg import Rec2100HLG
from .spaces.rec2100_linear import Rec2100Linear
from .spaces.jzazbz.css import Jzazbz
from .spaces.jzczhz.css import JzCzhz
from .spaces.ictcp.css import ICtCp
from .distance import DeltaE
from .distance.delta_e_76 import DE76
from .distance.delta_e_94 import DE94
from .distance.delta_e_cmc import DECMC
from .distance.delta_e_2000 import DE2000
from .distance.delta_e_hyab import DEHyAB
from .distance.delta_e_ok import DEOK
from .distance.delta_e_itp import DEITP
from .distance.delta_e_z import DEZ
from .contrast import ColorContrast
from .contrast.wcag21 import WCAG21Contrast
from .gamut import Fit
from .gamut.fit_minde_chroma import MINDEChroma
from .gamut.fit_lch_chroma import LChChroma
from .gamut.fit_oklch_chroma import OkLChChroma
from .gamut.fit_raytrace import RayTrace
from .gamut.fit_scale import Scale
from .gamut.fit_scale_luminance import ScaleLuminance
from .cat import CAT, Bradford
from .filters import Filter
from .filters.w3c_filter_effects import Sepia, Brightness, Contrast, Saturate, Opacity, HueRotate, Grayscale, Invert
from .filters.cvd import Protan, Deutan, Tritan
from .interpolate import Interpolator, Interpolate
from .interpolate.linear import Linear
from .interpolate.css_linear import CSSLinear
from .interpolate.continuous import Continuous
from .interpolate.bspline import BSpline
from .interpolate.bspline_natural import NaturalBSpline
from .interpolate.monotone import Monotone
from .temperature import CCT
from .temperature.ohno_2013 import Ohno2013
from .temperature.robertson_1968 import Robertson1968
from .types import Plugin
from typing import Iterator, overload, Sequence, Iterable, Any, Callable, Mapping, cast

if (3, 11) <= sys.version_info:
    from typing import Self
else:
    from typing_extensions import Self

SUPPORTED_CHROMATICITY_SPACES = {"xyz", "uv-1960", "uv-1976", "xy-1931"}

POSTFIX = {ANGLE_NULL: "", ANGLE_DEG: "deg", ANGLE_RAD: "rad", ANGLE_GRAD: "grad", ANGLE_TURN: "trun"}


class ColorMatch:
    """Color match object."""

    __slots__ = ("color", "start", "end")

    def __init__(self, color: Color, start: int, end: int) -> None:
        """Initialize."""
        pass

    def __str__(self) -> str:  # pragma: no cover
        """String."""
        pass

    __repr__ = __str__


class ColorMeta(abc.ABCMeta):
    """Ensure on subclass that the subclass has new instances of mappings."""

    def __init__(cls, name: str, bases: tuple[object, ...], clsdict: dict[str, Any]) -> None:
        """Copy mappings on subclass."""
        pass


class Color(metaclass=ColorMeta):
    """Color class object which provides access and manipulation of color spaces."""

    CS_MAP = {}  # type: dict[str, Space]
    DE_MAP = {}  # type: dict[str, DeltaE]
    FIT_MAP = {}  # type: dict[str, Fit]
    CAT_MAP = {}  # type: dict[str, CAT]
    CONTRAST_MAP = {}  # type: dict[str, ColorContrast]
    FILTER_MAP = {}  # type: dict[str, Filter]
    INTERPOLATE_MAP = {}  # type: dict[str, Interpolate]
    CCT_MAP = {}  # type: dict[str, CCT]
    PRECISION = util.DEF_PREC
    ROUNDING = util.DEF_ROUND_MODE
    FIT = util.DEF_FIT
    INTERPOLATE = util.DEF_INTERPOLATE
    INTERPOLATOR = util.DEF_INTERPOLATOR
    DELTA_E = util.DEF_DELTA_E
    HARMONY = util.DEF_HARMONY
    AVERAGE = util.DEF_AVERAGE
    CHROMATIC_ADAPTATION = util.DEF_CHROMATIC_ADAPTATION
    CONTRAST = util.DEF_CONTRAST
    CCT = util.DEF_CCT
    POWERLESS = False
    CARRYFORWARD = False

    # It is highly unlikely that a user would ever need to override this, but
    # just in case, it is exposed, but undocumented.
    #
    # This is meant to prevent infinite loops in the event that a user registers
    # poorly crafted color spaces with circular convert linkage or somehow doesn't
    # resolve to XYZ. 10 is a generous size as our current largest iteration chain
    # is 6, and increasing that past 10 seems highly unlikely:
    #    XYZ -> sRGB Linear -> sRGB -> HSL -> HSV -> HWB
    _MAX_CONVERT_ITERATIONS = 10

    def __init__(
        self, color: ColorInput, data: VectorLike | None = None, alpha: float = util.DEF_ALPHA, **kwargs: Any
    ) -> None:
        """Initialize."""
        pass

    def __len__(self) -> int:
        """Get number of channels."""
        pass

    def __iter__(self) -> Iterator[float]:
        """Initialize iterator."""
        pass

    @overload
    def __getitem__(self, i: str | int) -> float:
        pass

    @overload
    def __getitem__(self, i: slice) -> Vector:
        pass

    def __getitem__(self, i: str | int | slice) -> float | Vector:
        """Get channels."""
        pass

    @overload
    def __setitem__(self, i: str | int, v: float) -> None:
        pass

    @overload
    def __setitem__(self, i: slice, v: Vector) -> None:
        pass

    def __setitem__(self, i: str | int | slice, v: float | Vector) -> None:
        """Set channels."""
        pass

    def __eq__(self, other: Any) -> bool:
        """Compare equal."""
        pass

    @classmethod
    def _parse(
        cls, color: ColorInput, data: VectorLike | None = None, alpha: float = util.DEF_ALPHA, **kwargs: Any
    ) -> tuple[Space, Vector]:
        """Parse the color."""
        pass

    @classmethod
    def _match(
        cls, string: str, start: int = 0, fullmatch: bool = False
    ) -> tuple[Space, Vector, float, int, int] | None:
        """
        Match a color in a buffer and return a color object.

        This must return the color space, not the Color object.
        """
        pass

    @classmethod
    def match(cls, string: str, start: int = 0, fullmatch: bool = False) -> ColorMatch | None:
        """Match color."""
        pass

    @classmethod
    def _is_this_color(cls, obj: Any) -> bool:
        """Test if the input is "this" Color, not a subclass."""
        pass

    @classmethod
    def _is_color(cls, obj: Any) -> bool:
        """Test if the input is a Color."""
        pass

    @classmethod
    def register(cls, plugin: Plugin | Sequence[Plugin], *, overwrite: bool = False, silent: bool = False) -> None:
        """Register the hook."""
        pass

    @classmethod
    def deregister(cls, plugin: str | Sequence[str], *, silent: bool = False) -> None:
        """Deregister a plugin by name of specified plugin type."""
        pass

    @classmethod
    def random(cls, space: str, *, limits: Sequence[Sequence[float] | None] | None = None) -> Self:
        """Get a random color."""
        pass

    @classmethod
    def blackbody(
        cls,
        space: str,
        temp: float,
        duv: float = 0.0,
        *,
        method: str | None = None,
        scale: bool = True,
        scale_space: str | None = None,
        max_saturation: bool = True,
        clip_negative: bool = False,
        preserve_luminance: bool = False,
        **kwargs: Any,
    ) -> Self:
        """
        Get a color along the black body curve.

        Colors are specified by temperature in Kelvin. Depending on the algorithm, the practical
        range may differ.

        Colors are returned and normalized to be within the specified RGB space (preferably linear).
        The returned color, after normalization, is an approximation and may not exactly match the
        temperature. If `space` is set to `None` the color will not be normalized and may not be in
        the visible spectrum, but it should correlate with the specified temperature assuming it is
        not too far from the locus.
        """
        pass

    def cct(self, *, method: str | None = None, **kwargs: Any) -> Vector:
        """Get color temperature."""
        pass

    def to_dict(
        self, *, nans: bool = True, precision: int | Sequence[int] | None = None, rounding: str | None = None
    ) -> Mapping[str, Any]:
        """Return color as a data object."""
        pass

    def normalize(self, *, nans: bool = True) -> Self:
        """Normalize the color."""
        pass

    def is_nan(self, name: str) -> bool:  # pragma: no cover
        """Check if channel is NaN."""
        pass

    @classmethod
    def _handle_color_input(cls, color: ColorInput) -> Self:
        """Handle color input."""
        pass

    def space(self) -> str:
        """The current color space."""
        pass

    @classmethod
    def new(
        cls, color: ColorInput, data: VectorLike | None = None, alpha: float = util.DEF_ALPHA, **kwargs: Any
    ) -> Self:
        """Create new color object."""
        pass

    def clone(self) -> Self:
        """Clone."""
        pass

    def convert(self, space: str, *, fit: bool | str = False, in_place: bool = False, norm: bool = True) -> Self:
        """Convert to color space."""
        pass

    @contextmanager
    def within(self, space: str, *, norm: bool = True, norm_out: bool | None = None) -> Iterator[Self]:
        """Manipulate the color within the provided space while under context."""
        pass

    def is_achromatic(self) -> bool:
        """Test if color is achromatic."""
        pass

    def mutate(
        self, color: ColorInput, data: VectorLike | None = None, alpha: float = util.DEF_ALPHA, **kwargs: Any
    ) -> Self:
        """Mutate the current color to a new color."""
        pass

    def update(
        self,
        color: ColorInput,
        data: VectorLike | None = None,
        alpha: float = util.DEF_ALPHA,
        *,
        norm: bool = True,
        **kwargs: Any,
    ) -> Self:
        """Update the existing color space with the provided color."""
        pass

    def _hotswap(self, color: Color) -> Self:
        """
        Hot swap a color object.

        We expect it to be a color object, no special parsing, we just want to go fast.
        """
        pass

    def to_string(self, **kwargs: Any) -> str:
        """To string."""
        pass

    def __repr__(self) -> str:
        """Representation."""
        pass

    __str__ = __repr__

    def _repr_html_(self) -> str:  # pragma: no cover
        """
        Return an HTML representation of the color for Jupyter and other aware libraries.

        Colors are not gamut mapped, but returned as is.
        """
        pass

    def white(self, cspace: str = "xyz") -> Vector:
        """Get the white point."""
        pass

    def uv(self, mode: str = "1976", *, white: VectorLike | None = None) -> Vector:
        """Convert to `xy`."""
        pass

    def xy(self, *, white: VectorLike | None = None) -> Vector:
        """Convert to `xy`."""
        pass

    def Y(self, *, white: VectorLike | None = None) -> float:
        """Convert to `Y` (luminance)."""
        pass

    def split_chromaticity(self, cspace: str = "uv-1976", *, white: VectorLike | None = None) -> Vector:
        """
        Split a color into chromaticity and luminance coordinates.

        Colors are split under the XYZ color space using the current color's white point.
        If results are desired relative to a different white point, one can be provided.
        """
        pass

    @classmethod
    def chromaticity(
        cls,
        space: str,
        coords: VectorLike,
        cspace: str = "uv-1976",
        *,
        white: VectorLike | None = None,
        scale: bool = False,
        scale_space: str | None = None,
        max_saturation: bool = False,
        clip_negative: bool = False,
        preserve_luminance: bool = False,
    ) -> Self:
        """
        Create a color from chromaticity coordinates.

        A luminance of 1 will be assumed unless luminance is included with the coordinates.
        The relative white point of the chromaticity coordinates will be assumed as the
        targeted color space unless one is provided via `white`.

        Lastly, colors can be scaled/normalized within a linear RGB space to normalize
        luminance and provide a nice viewable color. This is useful when the luminance is
        not accurate (such as when luminance is assumed 1). Colors that are out of the linear
        RGB space's gamut will only be rough approximations of the color due to gamut
        limitations. Default linear RGB space is linear sRGB.
        """
        pass

    @classmethod
    def convert_chromaticity(
        cls, cspace1: str, cspace2: str, coords: VectorLike, *, white: VectorLike | None = None
    ) -> Vector:
        """
        Convert to or from chromaticity coordinates or between other chromaticity coordinates.

        When converting to or from chromaticity coordinates, the coordinates must be in the XYZ space.
        A white point can be provided and only serves to align colors like black on the achromatic axis;
        otherwise, black will be returned as [0, 0] for the two respective chromaticity points.
        """
        pass

    @classmethod
    def chromatic_adaptation(
        cls, w1: VectorLike, w2: VectorLike, xyz: VectorLike, *, method: str | None = None
    ) -> Vector:
        """Chromatic adaptation."""
        pass

    def clip(self, space: str | None = None) -> Self:
        """Clip the color channels."""
        pass

    def fit(self, space: str | None = None, *, method: str | None = None, **kwargs: Any) -> Self:
        """Fit the gamut using the provided method."""
        pass

    def in_gamut(self, space: str | None = None, *, tolerance: float | None = None, **kwargs: Any) -> bool:
        """Check if current color is in gamut."""
        pass

    def in_pointer_gamut(self, *, tolerance: float = util.DEF_FIT_TOLERANCE) -> bool:  # pragma: no cover
        """Check if in pointer gamut."""
        pass

    def fit_pointer_gamut(self) -> Self:  # pragma: no cover
        """Check if in pointer gamut."""
        pass

    def mask(self, channel: str | Sequence[str], *, invert: bool = False, in_place: bool = False) -> Self:
        """Mask color channels."""
        pass

    def mix(
        self, color: ColorInput, percent: float = util.DEF_MIX, *, in_place: bool = False, **interpolate_args: Any
    ) -> Self:
        """
        Mix colors using interpolation.

        This uses the interpolate method to find the center point between the two colors.
        The basic mixing logic is outlined in the CSS level 5 draft.
        """
        pass

    @classmethod
    def steps(
        cls,
        colors: Sequence[ColorInput | interpolate.stop | Callable[..., float]],
        *,
        steps: int = 2,
        max_steps: int = 1000,
        max_delta_e: float = 0,
        delta_e: str | None = None,
        delta_e_args: dict[str, Any] | None = None,
        **interpolate_args: Any,
    ) -> list[Self]:
        """Discrete steps."""
        pass

    @classmethod
    def discrete(
        cls,
        colors: Sequence[ColorInput | interpolate.stop | Callable[..., float]],
        *,
        space: str | None = None,
        out_space: str | None = None,
        steps: int | None = None,
        max_steps: int = 1000,
        max_delta_e: float = 0,
        delta_e: str | None = None,
        delta_e_args: dict[str, Any] | None = None,
        domain: Vector | None = None,
        **interpolate_args: Any,
    ) -> Interpolator[Self]:
        """Create a discrete interpolation."""
        pass

    @classmethod
    def interpolate(
        cls,
        colors: Sequence[ColorInput | interpolate.stop | Callable[..., float]],
        *,
        space: str | None = None,
        out_space: str | None = None,
        progress: Mapping[str, Callable[..., float]] | Callable[..., float] | None = None,
        hue: str = util.DEF_HUE_ADJ,
        premultiplied: bool = True,
        extrapolate: bool = False,
        domain: Vector | None = None,
        method: str | None = None,
        padding: float | tuple[float, float] | None = None,
        carryforward: bool | None = None,
        powerless: bool | None = None,
        **kwargs: Any,
    ) -> Interpolator[Self]:
        """
        Return an interpolation function.

        The function will return an interpolation function that accepts a value (which should
        be in the range of [0..1] and will return a color based on that value.

        While we use NaNs to mask off channels when doing the interpolation, we do not allow
        arbitrary specification of NaNs by the user, they must specify channels via `adjust`
        if they which to target specific channels for mixing. Null hues become NaNs before
        mixing occurs.
        """
        pass

    @classmethod
    def weighted_mix(
        cls,
        colors: Sequence[ColorInput],
        weights: Sequence[float] | None = None,
        *,
        space: str | None = None,
        out_space: str | None = None,
        method: str | None = None,
        premultiplied: bool = True,
        carryforward: bool = False,
        powerless: bool = False,
        hue: str = "shorter",
        **kwargs: Any,
    ) -> Self:
        """Perform a weighted mix of multiple colors."""
        pass

    @classmethod
    def average(
        cls,
        colors: Iterable[ColorInput],
        weights: Iterable[float] | None = None,
        *,
        space: str | None = None,
        out_space: str | None = None,
        premultiplied: bool = True,
        carryforward: bool | None = False,
        **kwargs: Any,
    ) -> Self:
        """Average the colors."""
        pass

    def filter(  # noqa: A003
        self,
        name: str,
        amount: float | None = None,
        *,
        space: str | None = None,
        out_space: str | None = None,
        in_place: bool = False,
        **kwargs: Any,
    ) -> Self:
        """Filter."""
        pass

    def harmony(
        self, name: str, *, space: str | None = None, out_space: str | None = None, **kwargs: Any
    ) -> list[Self]:
        """Acquire the specified color harmonies."""
        pass

    @classmethod
    def layer(
        cls,
        colors: Sequence[ColorInput],
        *,
        blend: str | bool = "normal",
        operator: str | bool = "source-over",
        space: str | None = None,
        out_space: str | None = None,
    ) -> Self:
        """
        Apply color compositing (blend modes and alpha blending) on a list of colors.

        Colors are overlaid on each other with left being the top of the stack and right being the bottom of the stack.
        """
        pass

    def delta_e(self, color: ColorInput, *, method: str | None = None, **kwargs: Any) -> float:
        """Delta E distance."""
        pass

    def distance(self, color: ColorInput, *, space: str = "lab") -> float:
        """Delta."""
        pass

    def closest(self, colors: Sequence[ColorInput], *, method: str | None = None, **kwargs: Any) -> Self:
        """Find the closest color to the current base color."""
        pass

    def luminance(self, *, white: VectorLike | None = cat.WHITES["2deg"]["D65"]) -> float:
        """Get color's luminance."""
        pass

    def contrast(self, color: ColorInput, method: str | None = None) -> float:
        """Compare the contrast ratio of this color and the provided color."""
        pass

    def wavelength(
        self, *, white: VectorLike | None = None, complementary: bool = False
    ) -> tuple[float, Vector, Vector]:
        """Get the dominant wavelength."""
        pass

    @classmethod
    def from_wavelength(
        cls,
        space: str,
        wavelength: float,
        *,
        white: VectorLike | None = None,
        scale: bool = True,
        scale_space: str | None = None,
        max_saturation: bool = True,
        clip_negative: bool = False,
        preserve_luminance: bool = False,
    ) -> Self:
        """Create a color from a wavelength."""
        pass

    @overload
    def get(
        self, name: str, *, nans: bool = ..., precision: int | Sequence[int] | None = ..., rounding: str | None = ...
    ) -> float:
        pass

    @overload
    def get(
        self,
        name: list[str] | tuple[str, ...],
        *,
        nans: bool = ...,
        precision: int | Sequence[int] | None = ...,
        rounding: str | None = ...,
    ) -> Vector:
        pass

    def get(
        self,
        name: str | list[str] | tuple[str, ...],
        *,
        nans: bool = True,
        precision: int | Sequence[int] | None = None,
        rounding: str | None = None,
    ) -> float | Vector:
        """Get channel."""
        pass

    def set(  # noqa: A003
        self,
        name: str | dict[str, float | Callable[..., float]],
        value: float | Callable[..., float] | None = None,
        *,
        nans: bool = True,
    ) -> Self:
        """Set channel."""
        pass

    def coords(
        self, *, nans: bool = True, precision: int | Sequence[int] | None = None, rounding: str | None = None
    ) -> Vector:
        """Get the color channels and optionally remove undefined values."""
        pass

    def alpha(self, *, nans: bool = True, precision: int | None = None, rounding: str | None = None) -> float:
        """Get the alpha channel."""
        pass


try:
    Color.register(
        [
            # Spaces
            XYZD65(),
            XYZD50(),
            sRGB(),
            sRGBLinear(),
            DisplayP3(),
            DisplayP3Linear(),
            Oklab(),
            OkLCh(),
            Lab(),
            LCh(),
            LabD65(),
            LChD65(),
            Jzazbz(),
            JzCzhz(),
            ICtCp(),
            HSV(),
            HSL(),
            HWB(),
            Rec2020(),
            Rec2020Linear(),
            Rec2100PQ(),
            Rec2100HLG(),
            Rec2100Linear(),
            A98RGB(),
            A98RGBLinear(),
            ProPhotoRGB(),
            ProPhotoRGBLinear(),
            # CAT
            Bradford(),
            # Delta E
            DE76(),
            DE94(),
            DECMC(),
            DE2000(),
            DEHyAB(),
            DEOK(),
            DEITP(),
            DEZ(),
            # Fit
            MINDEChroma(),
            LChChroma(),
            OkLChChroma(),
            RayTrace(),
            Scale(),
            ScaleLuminance(),
            # Filters
            Sepia(),
            Brightness(),
            Contrast(),
            Saturate(),
            Opacity(),
            HueRotate(),
            Grayscale(),
            Invert(),
            Protan(),
            Deutan(),
            Tritan(),
            # Contrast
            WCAG21Contrast(),
            # Interpolation
            Linear(),
            CSSLinear(),
            Continuous(),
            BSpline(),
            NaturalBSpline(),
            Monotone(),
            # CCT
            Robertson1968(),
            Ohno2013(),
        ]
    )
except (NotImplementedError, TypeError, AttributeError):
    pass
