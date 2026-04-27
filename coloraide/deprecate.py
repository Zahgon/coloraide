"""Deprecation functions."""
from __future__ import annotations
import warnings
from functools import wraps
from typing import Any, Callable


def deprecated(message: str, stacklevel: int = 2) -> Callable[..., Any]:
    """
    Raise a `DeprecationWarning` when wrapped function/method is called.

    Usage:

        @deprecated("This method will be removed in version X; use Y instead.")
        def some_method()"
            pass
    """
    pass


def warn_deprecated(message: str, stacklevel: int = 2) -> None:
    """Warn deprecated."""
    pass
