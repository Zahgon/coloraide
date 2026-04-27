"""Color base."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from ..channels import Channel
from ..css import serialize
from ..types import VectorLike, Vector, Plugin
from .. import deprecate
from typing import Any, TYPE_CHECKING, Callable, Sequence
import math

if TYPE_CHECKING:  # pragma: no cover
    from ..color import Color

__deprecated__ = {
    "Regular": "Prism"
}


def __getattr__(name: str) -> Any:  # pragma: no cover
    """Warn for deprecated attributes."""
    pass


class Prism:
    """Prism is a 3D rectangular prism."""


class RGBish(Prism):
    """RGB-ish space."""


class Cylindrical:
    """Cylindrical space."""

    get_channel_index: Callable[[str], int]

    def radial_name(self) -> str:
        """Radial name."""

        return "s"

    def hue_name(self) -> str:
        """Hue channel name."""

        return "h"

    def hue_index(self) -> int:  # pragma: no cover
        """Get hue index."""
        pass

    def radial_index(self) -> int:  # pragma: no cover
        """Get radial index."""
        pass


class Luminant:
    """A space that contains luminance or luminance-like component."""

    get_channel_index: Callable[[str], int]

    def lightness_name(self) -> str:
        """Lightness name."""

        return "l"

    def lightness_index(self) -> int:
        """Get lightness index."""
        pass


class HSLish(Luminant, Cylindrical):
    """HSL-ish space."""


class HSVish(Luminant, Cylindrical):
    """HSV-ish space."""


class HWBish(Cylindrical):
    """HWB-ish space."""

    def radial_name(self) -> str:
        """Radial name."""

        return "w"


class Labish(Luminant, Prism):
    """Lab-ish color spaces."""


class LChish(Luminant, Cylindrical):
    """LCh-ish color spaces."""

    def radial_name(self) -> str:
        """Radial name."""

        return "c"


alpha_channel = Channel('alpha', 0.0, 1.0, bound=True, limit=(0.0, 1.0))


class SpaceMeta(ABCMeta):
    """Ensure on subclass that the subclass has new instances of mappings."""

    def __init__(cls, name: str, bases: tuple[object, ...], clsdict: dict[str, Any]) -> None:
        """Copy mappings on subclass."""
        pass


class Space(Plugin, metaclass=SpaceMeta):
    """Base color space object."""

    BASE = ""  # type: str
    # Color space name
    NAME = ""
    # Serialized name
    SERIALIZE = ()  # type: tuple[str, ...]
    # Channel names
    CHANNELS = ()  # type: tuple[Channel, ...]
    # Channel aliases
    CHANNEL_ALIASES = {}  # type: dict[str, str]
    # Enable or disable default color format parsing and serialization.
    COLOR_FORMAT = True
    # Some color spaces are a transform of a specific RGB color space gamut, e.g. HSL has a gamut of sRGB.
    # When testing or gamut mapping a color within the current color space's gamut, `GAMUT_CHECK` will
    # declare which space must be used as reference if anything other than the current space is required.
    #
    # Specifically, when testing if a color is in gamut, both the origin space and the specified gamut
    # space will be checked as sometimes a color is within the threshold of being "close enough" to the gamut,
    # but the color can still be far outside the origin space's coordinates. Checking both ensures sane values
    # that are also close enough to the gamut.
    #
    # When actually gamut mapping, only the gamut space is used, if none is specified, the origin space is used.
    GAMUT_CHECK = None  # type: str | None
    # `CLIP_SPACE` forces a different space to be used for clipping than what is specified by `GAMUT_CHECK`.
    # This is used in cases like HSL where the `GAMUT_CHECK` space is sRGB, but we want to clip in HSL as it
    # is still reasonable and faster.
    CLIP_SPACE = None  # type: str | None
    # White point
    WHITE = (0.0, 0.0)
    # What is the color space's dynamic range
    DYNAMIC_RANGE = 'sdr'
    # Is the space subtractive
    SUBTRACTIVE = False

    def __init__(self, **kwargs: Any) -> None:
        """Initialize."""
        pass

    def names(self) -> tuple[Channel, ...]:
        """Returns component names in a logical order specific to their color space type."""
        pass

    def indexes(self) -> list[int]:
        """Returns component indexes in a logical order specific to their color space type."""
        pass

    def is_polar(self) -> bool:
        """Return if the space is polar."""
        pass

    def linear(self) -> str:
        """Will return the name of the space which is the linear version of itself (if available)."""

        return ''

    def get_channel_index(self, name: str) -> int:
        """Get channel index."""
        pass

    def resolve_channel(self, index: int, coords: Vector) -> float:
        """Resolve channels."""
        pass

    def _serialize(self) -> tuple[str, ...]:
        """Get the serialized name."""
        pass

    def normalize(self, coords: Vector) -> Vector:
        """
        Normalize coordinates.

        This allows a color space to normalize valid, but non-standard coordinates.
        An example is cylindrical spaces with negative chroma/saturation. Such models
        often have a valid, positive chroma/saturation and hue configuration that
        matches the same color.
        """
        pass

    def is_achromatic(self, coords: Vector) -> bool | None:  # pragma: no cover
        """Check if color is achromatic."""

        return None

    @classmethod
    def white(cls) -> VectorLike:
        """Get the white color for this color space."""
        pass

    @abstractmethod
    def to_base(self, coords: Vector) -> Vector:  # pragma: no cover
        """To base color."""

    @abstractmethod
    def from_base(self, coords: Vector) -> Vector:  # pragma: no cover
        """From base color."""

    def to_string(
        self,
        parent: Color,
        *,
        alpha: bool | None = None,
        precision: int | Sequence[int] | None = None,
        rounding: str | None = None,
        fit: str | bool | dict[str, Any] = True,
        none: bool = False,
        percent: bool | Sequence[bool] = False,
        angle: str = 'deg',
        **kwargs: Any
    ) -> str:
        """Convert to CSS 'color' string: `color(space coords+ / alpha)`."""
        pass

    def match(
        self,
        string: str,
        start: int = 0,
        fullmatch: bool = True
    ) -> tuple[tuple[Vector, float], int] | None:
        """Match a color by string."""

        return None
