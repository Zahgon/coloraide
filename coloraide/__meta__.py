"""Meta related things."""
from __future__ import annotations
from typing import NamedTuple
import re

RE_VER = re.compile(
    r'''(?x)
    (?P<major>\d+)(?:\.(?P<minor>\d+))?(?:\.(?P<micro>\d+))?
    (?:(?P<type>a|b|rc)(?P<pre>\d+))?
    (?:\.post(?P<post>\d+))?
    (?:\.dev(?P<dev>\d+))?
    '''
)

REL_MAP = {
    ".dev": "",
    ".dev-alpha": "a",
    ".dev-beta": "b",
    ".dev-candidate": "rc",
    "alpha": "a",
    "beta": "b",
    "candidate": "rc",
    "final": ""
}

DEV_STATUS = {
    ".dev": "2 - Pre-Alpha",
    ".dev-alpha": "2 - Pre-Alpha",
    ".dev-beta": "2 - Pre-Alpha",
    ".dev-candidate": "2 - Pre-Alpha",
    "alpha": "3 - Alpha",
    "beta": "4 - Beta",
    "candidate": "4 - Beta",
    "final": "5 - Production/Stable"
}

PRE_REL_MAP = {"a": 'alpha', "b": 'beta', "rc": 'candidate'}


class VersionSpec(NamedTuple):
    """Version specification."""

    major: int
    minor: int
    micro: int
    release: str
    pre: int
    post: int
    dev: int


class Version(VersionSpec):
    """
    Get the version (PEP 440).

    A biased approach to the PEP 440 semantic version.

    Provides a tuple structure which is sorted for comparisons `v1 > v2` etc.
      (major, minor, micro, release type, pre-release build, post-release build, development release build)
    Release types are named in is such a way they are comparable with ease.
    Accessors to check if a development, pre-release, or post-release build. Also provides accessor to get
    development status for setup files.

    How it works (currently):

    - You must specify a release type as either `final`, `alpha`, `beta`, or `candidate`.
    - To define a development release, you can use either `.dev`, `.dev-alpha`, `.dev-beta`, or `.dev-candidate`.
      The dot is used to ensure all development specifiers are sorted before `alpha`.
      You can specify a `dev` number for development builds, but do not have to as implicit development releases
      are allowed.
    - You must specify a `pre` value greater than zero if using a prerelease as this project (not PEP 440) does not
      allow implicit prereleases.
    - You can optionally set `post` to a value greater than zero to make the build a post release. While post releases
      are technically allowed in prereleases, it is strongly discouraged, so we are rejecting them. It should be
      noted that we do not allow `post0` even though PEP 440 does not restrict this. This project specifically
      does not allow implicit post releases.
    - It should be noted that we do not support epochs `1!` or local versions `+some-custom.version-1`.

    Acceptable version releases:

    ```
    Version(1, 0, 0, "final")                    1.0
    Version(1, 2, 0, "final")                    1.2
    Version(1, 2, 3, "final")                    1.2.3
    Version(1, 2, 0, "alpha", pre=4)             1.2a4
    Version(1, 2, 0, "beta", pre=4)              1.2b4
    Version(1, 2, 0, "candidate", pre=4)         1.2rc4
    Version(1, 2, 0, "final", post=1)            1.2.post1
    Version(1, 2, 3, ".dev")                     1.2.3.dev0
    Version(1, 2, 3, ".dev", dev=1)              1.2.3.dev1
    ```
    """

    def __new__(
        cls,
        major: int, minor: int, micro: int, release: str = "final",
        pre: int = 0, post: int = 0, dev: int = 0
    ) -> Version:
        """Validate version info."""
        pass

    def _is_pre(self) -> bool:
        """Is prerelease."""
        pass

    def _is_dev(self) -> bool:
        """Is development."""
        pass

    def _is_post(self) -> bool:
        """Is post."""
        pass

    def _get_dev_status(self) -> str:  # pragma: no cover
        """Get development status string."""
        pass

    def _get_canonical(self) -> str:
        """Get the canonical output string."""
        pass


def parse_version(ver: str) -> Version:
    """Parse version into a comparable Version tuple."""
    pass


try:
    __version_info__ = Version(8, 9, 0, "final")
    __version__ = __version_info__._get_canonical()
except (NotImplementedError, TypeError, AttributeError):
    __version_info__ = None  # type: ignore[assignment]
    __version__ = "0.0.0"
