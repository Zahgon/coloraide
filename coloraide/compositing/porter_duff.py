"""Porter Duff compositing."""
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class PorterDuff(metaclass=ABCMeta):
    """Porter Duff compositing."""

    def __init__(self, cba: float, csa: float) -> None:
        """Initialize."""
        pass

    @abstractmethod
    def fa(self) -> float:  # pragma: no cover
        """Calculate `Fa`."""
        pass

    @abstractmethod
    def fb(self) -> float:  # pragma: no cover
        """Calculate `Fb`."""
        pass

    def co(self, cb: float, cs: float) -> float:
        """Calculate premultiplied coordinate."""
        pass

    def ao(self) -> float:
        """Calculate output alpha."""
        pass


class Clear(PorterDuff):
    """Clear."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class Copy(PorterDuff):
    """Copy."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class Destination(PorterDuff):
    """Destination."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class SourceOver(PorterDuff):
    """Source over."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class DestinationOver(PorterDuff):
    """Destination over."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class SourceIn(PorterDuff):
    """Source in."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class DestinationeIn(PorterDuff):
    """Destination in."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class SourceOut(PorterDuff):
    """Source out."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class DestinationOut(PorterDuff):
    """Destination out."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class SourceAtop(PorterDuff):
    """Source atop."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class DestinationAtop(PorterDuff):
    """Destination atop."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class XOR(PorterDuff):
    """XOR."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class Lighter(PorterDuff):
    """Lighter."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass


class PlusDarker(PorterDuff):
    """Plus darker."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass

    def co(self, cb: float, cs: float) -> float:
        """Calculate premultiplied coordinate."""
        pass

    def ao(self) -> float:
        """Calculate output alpha."""
        pass


class PlusLigher(PorterDuff):
    """Plus lighter."""

    def fa(self) -> float:
        """Calculate `Fa`."""
        pass

    def fb(self) -> float:
        """Calculate `Fb`."""
        pass

    def co(self, cb: float, cs: float) -> float:
        """Calculate premultiplied coordinate."""
        pass

    def ao(self) -> float:
        """Calculate output alpha."""
        pass


SUPPORTED = {
    'clear': Clear,
    'copy': Copy,
    'destination': Destination,
    'source-over': SourceOver,
    'destination-over': DestinationOver,
    'source-in': SourceIn,
    'destination-in': DestinationeIn,
    'source-out': SourceOut,
    'destination-out': DestinationOut,
    'source-atop': SourceAtop,
    'destination-atop': DestinationAtop,
    'xor': XOR,
    'lighter': Lighter,
    'plus-darker': PlusDarker,
    'plus-lighter': PlusLigher
}


def compositor(name: str) -> type[PorterDuff]:
    """Get the requested compositor."""
    pass
