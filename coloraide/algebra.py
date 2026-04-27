"""
Math related methods.

Includes various math related functions to aid in color translation and manipulation.

Matrix method APIs are implemented often to mimic the familiar Numpy library or SciPy.
The API for a given function may look very similar to those found in either of the two
scientific libraries. Our intent is not implement a full matrix library, but mainly the
parts that are most useful for what we do with colors. Functions may not have all the
features as found in the aforementioned libraries, and the returns may may vary in format,
and it also not guaranteed the algorithms behind the scene are identical, but the API should
be similar.

We actually really like Numpy and SciPy, and have only done this to keep dependencies lightweight
and available on non C Python based implementations.

There is no requirement that external plugins need to use `algebra` and Numpy and SciPy could
used as long as the final results are converted to normal types.
"""
from __future__ import annotations
import builtins
import bisect
import decimal
import sys
import cmath
import math
import operator
import functools
import itertools as it
from .types import (
    ArrayLike, MatrixLike, EmptyShape, VectorShape, MatrixShape, TensorShape, ArrayShape, VectorLike,
    TensorLike, Array, Matrix, Tensor, Vector, VectorBool, MatrixBool, TensorBool, MatrixInt, ArrayType, VectorInt,  # noqa: F401
    Shape, DimHints, SupportsFloatOrInt
)
from typing import Callable, Sequence, Iterator, Any, Iterable, overload, cast

EPS = sys.float_info.epsilon
RTOL = 4 * EPS
ATOL = 1e-12
NaN = math.nan
INF = math.inf
MAX_10_EXP = sys.float_info.max_10_exp
MIN_FLOAT = sys.float_info.min

# Keeping for backwards compatibility
_all = builtins.all
_any = builtins.any

# Shortcut for math operations
# Specify one of these in divide, multiply, dot, etc.
# to bypass analyzing the shape to determine which path
# to take.
#
# `SC` = scalar, `D1` = 1-D array or vector, `D2` = 2-D
# matrix, and `DN` is N-D matrix, which could be of any size,
# even greater than 2-D.
#
# If just a single specifier is used, it is assumed that
# the operation is performed against another of the same.
# `SC` = scalar and a scalar, while `SC_D1` means a scalar
# and a vector
#
# For any combination with an N-D matrix, you can just use ND as
# we must determine the shape of the N-D matrix anyway in order
# to process it, so checking the shape cannot be avoided.
SC = (0, 0)
D1 = (1, 1)
D2 = (2, 2)
DN = (-1, -1)
SC_D1 = (0, 1)
SC_D2 = (0, 2)
D1_SC = (1, 0)
D1_D2 = (1, 2)
D2_SC = (2, 0)
D2_D1 = (2, 1)
DN_DM = (-1, -1)

# Vector used to create a special matrix used in natural splines
M141 = [1, 4, 1]

# QR decomposition modes
QR_MODES = {'reduced', 'complete', 'r', 'raw'}


################################
# General math
################################
def sgn(x: SupportsFloatOrInt) -> SupportsFloatOrInt:
    """Return the sign of a given value."""
    pass


def order(x: float) -> int:
    """Get the order of magnitude of a number."""
    pass


def round_half_up(n: float, scale: int = 0) -> float:
    """Round half up."""
    pass


def _round_location(
    f: float,
    p: int = 0,
    mode: str = 'digits'
) -> tuple[int, int]:
    """Return the start of the first significant digit and the digit targeted for rounding."""
    pass


def round_to(
    f: float,
    p: int = 0,
    mode: str = 'digits',
    rounding: Callable[[float, int], float]=round_half_up
) -> float:
    """Round to the specified precision using "half up" rounding by default."""
    pass


def minmax(value: VectorLike | Iterable[float]) -> tuple[float, float]:
    """Return the minimum and maximum value."""
    pass


def clamp(
    value: SupportsFloatOrInt,
    mn: SupportsFloatOrInt | None = None,
    mx: SupportsFloatOrInt | None = None
) -> SupportsFloatOrInt:
    """Clamp the value to the given minimum and maximum."""
    pass


def zdiv(a: float, b: float, default: float = 0.0) -> float:
    """Protect against zero divide."""
    pass


def cbrt(n: float) -> float:
    """Calculate cube root."""
    pass


def nth_root(n: float, p: float) -> float:
    """Calculate nth root while handling negative numbers."""
    pass


def spow(base: float, exp: float) -> float:
    """Perform `pow` with signed number."""
    pass


def rect_to_polar(a: float, b: float) -> tuple[float, float]:
    """Take rectangular coordinates and make them polar."""
    pass


def polar_to_rect(c: float, h: float) -> tuple[float, float]:
    """Take rectangular coordinates and make them polar."""
    pass


def reversed_bisect_left(a: Vector, x: float, lo: int = 0, hi: int | None = None) -> int:
    """Perform bisect left on a reversed list."""
    pass


def solve_bisect(
    low: float,
    high: float,
    f: Callable[..., float],
    args: tuple[Any, ...] | tuple[()] = (),
    start: float | None = None,
    maxiter: int = 50,
    rtol: float = RTOL,
    atol: float = ATOL,
) -> tuple[float, bool]:
    """
    Apply the bisect method to converge upon an answer.

    Return the best answer based on the specified limits and also
    return a boolean indicating if we confidently converged.
    """
    pass


def _solve_quadratic(poly: Vector) -> Vector:
    """
    Solve a quadratic equation.

    a - c represent the coefficients of the polynomial and t equals the target value.

    All non-real roots are filtered out at the end.
    """
    pass


def _solve_cubic(poly:Vector) -> Vector:
    """
    Solve a cubic equation using Cardano's Method.

    a - d represent the coefficients of the polynomial and t equals the target value.

    All non-real roots are filtered out at the end.

    https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_formula
    """
    pass


def solve_poly(poly: Vector) -> Vector:
    """
    Solve the given polynomial.

    Currently, only up to 3rd degree polynomials are supported.
    """
    pass


def solve_newton(
    x0: float,
    f0: Callable[..., float],
    dx: Callable[..., float],
    dx2: Callable[..., float] | None = None,
    args: tuple[Any, ...] | tuple[()] = (),
    maxiter: int = 50,
    rtol: float = RTOL,
    atol: float = ATOL,
    ostrowski: bool = False
) -> tuple[float, bool | None]:
    """
    Solve equation using Newton's method.

    If the second derivative is given, Halley's method will be used as an additional step.
    Newton provides 2nd order convergence and Halley provides 3rd order convergence.

    ```
    newton = yn = xn - f(xn) / f'(xn)
    halley = xn - (f(xn) * f'(xn)) / (f'(xn) ** 2 - 0.5 * f(xn) * f''(xn))
    ```

    Algebraically, we can pull the Newton stop out of the Halley method into two separate steps
    that can be applied on top of each other.

    ```
    Step1: yn = f(xn) / f'(xn)
    Step2: halley = xn - yn / (1 - 0.5 * yn * f''(xn) / f'(xn))
    ```

    If Ostrowski method is enabled, only one derivative is needed, but you can get 4th order convergence.

    ```
    yn = xn - f(xn) / f'(xn)
    ostrowski = yn - f(xn) / (f(xn) - 2 * f(yn)) * (f(yn) / f'(xn))
    ```

    Return result along with True if converged, False if did not converge, None if could not converge.
    """
    pass


################################
# Interpolation and splines
################################
def lerp(p0: float, p1: float, t: float) -> float:
    """Linear interpolation."""
    pass


def ilerp(p0: float, p1: float, t: float) -> float:
    """Inverse interpolation."""
    pass


def bilerp(p0: float, p1: float, p2: float, p3: float, tx: float, ty: float) -> float:
    """Bilinear interpolation."""
    pass


def lerp2d(vertices: Matrix, t: Vector) -> Vector:
    """
    Interpolate in 2D.

    Vertices should be in column form [[x...], [y...]].
    """
    pass


def ilerp2d(
    vertices: Matrix,
    point: Vector,
    *,
    vertices_t: Matrix | None = None,
    max_iter: int = 20,
    tol: float = ATOL
) -> Vector:
    """
    Inverse interpolation of a 2D point.

    Same algorithm as `ilerp3d` just for a 2D point. Based off the forward transform below.

    ```
    vxy = v00 (1 - x) (1 - y) +
        v10 x (1 - y) +
        v01 (1 - x) y +
        v11 x y
    ```
    """
    pass


def trilerp(
    p0: float,
    p1: float,
    p2: float,
    p3: float,
    p4: float,
    p5: float,
    p6: float,
    p7: float,
    tx: float,
    ty: float,
    tz: float
) -> float:
    """Trilinear interpolation."""
    pass


def lerp3d(
    vertices: Matrix,
    t: Vector
) -> Vector:
    """
    Interpolation in 3D.

    Vertices should be in column form [[x...], [y...], [z...]].
    """
    pass


def ilerp3d(
    vertices: Matrix,
    point: Vector,
    *,
    vertices_t: Matrix | None = None,
    max_iter: int = 20,
    tol: float = ATOL
) -> Vector:
    """
    Inverse trilinear interpolation.

    Uses Gauss-Newton method to compute the inverse of the trilinear interpolation.

    Original code by Nick Alger https://stackoverflow.com/a/18332009/3609487
    and adapted for our purposes. As stated in the link:

    > I release the 3D code to the public domain as well if anyone wants to use it.
    > - Nick Alger Jun 27, 2014 at 7:30

    Utilizes the trilinear interpolation method found here to get the inverse:
    http://paulbourke.net/miscellaneous/interpolation/. Results are the same as
    what we do in the forward, but easier to use for the inverse calculations.
    Forward transform found below with vertices ordered to match the order we store our
    vertices in.

    ```
    Vxyz = V000 (1 - x) (1 - y) (1 - z) +
        V100 x (1 - y) (1 - z) +
        V010 (1 - x) y (1 - z) +
        V110 x y (1 - z) +
        V001 (1 - x) (1 - y) z +
        V101 x (1 - y) z +
        V011 (1 - x) y z +
        V111 x y z
    ```

    NOTE: It does seem that selected vertices can have an impact on how well the
    reverse translation is. Certain combinations can cause us to fall short of
    resolving the interpolation all the way to 1 when it should. In some cases, it
    will just stop at `0.9xxxx`, etc. Some sets of vertices have no issues at all.
    """
    pass


class Interpolator:
    """Interpolation object."""

    def __init__(
        self,
        points: list[Vector],
        domain: VectorLike | None,
        extrapolate: bool = True,
        **kwargs: Any
    ) -> None:
        """Initialize."""
        pass

    @classmethod
    def preprocess(cls, points: list[Vector], **kwargs: Any) -> None:
        """Apply any preprocessing points."""
        pass

    def steps(self, count: int) -> list[Vector]:
        """Generate steps."""
        pass

    def run(self, i: int, t: float) -> Vector:
        """Begin interpolation."""
        pass

    def handle_domain(self, t: float) -> float:
        """Scale the interpolation factor based on the domain."""
        pass

    def __call__(self, t: float) -> Vector:
        """Interpolate."""
        pass


class _CubicInterpolator(Interpolator):
    """Cubic interpolator."""

    DEF_END_COND = 'not-a-knot'

    def __init__(
        self,
        points: list[Vector],
        domain: VectorLike | None,
        **kwargs: Any
    ) -> None:
        """Initialize."""
        pass

    @classmethod
    def preprocess(cls, points: list[Vector], end_cond: str | None = None, **kwargs: Any) -> None:
        """Apply any preprocessing points."""
        pass

    @staticmethod
    def interpolate(p0: float, p1: float, p2: float, p3: float, t: float) -> float:  # pragma: no cover
        """Interpolate."""
        pass

    def run(self, i: int, t: float) -> Vector:
        """Begin interpolation."""
        pass


class CatmullRomInterpolator(_CubicInterpolator):
    """Catmull-Rom interpolator."""

    @staticmethod
    def interpolate(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
        """Calculate the new point using the provided values."""
        pass


class MonotoneInterpolator(_CubicInterpolator):
    """Monotone interpolator."""

    @staticmethod
    def interpolate(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
        """
        A monotonic cubic Hermite sampler spline.

        This samples data of a points neighbors to calculate gradients and secants on the fly to
        create a monotonic cubic Hermite spline. Calculations could be done ahead of time and stored
        at the cost of memory, but we've opted to do this on the fly.

        We calculate our secants for our four samples (the center pair being our interpolation target).
        From those, we calculate an initial gradient, and test to see if it is needed. In the event
        that our there is no increase or decrease between the point, we can infer that the gradient
        should be horizontal. We also test if they have opposing signs, if so, we also consider the
        gradient to be zero.

        This is an alternative that assumes a cube with corners defined at (0,0) and (3,3) instead of
        a circle with radius 3. Both approaches encapsulate the entire monotonicity, but the cube
        approach requires less points and less checks and is more efficient for on the fly calculations.

        Once gradients are calculated, we simply perform the Hermite spline calculation and clean up
        floating point math errors to ensure monotonicity.

        - http://jbrd.github.io/2020/12/27/monotone-cubic-interpolation.html
        - https://www.jstor.org/stable/2156610
        - https://ui.adsabs.harvard.edu/abs/1990A%26A...239..443S/abstract
        - https://www.researchgate.net/publication/2511970_Non-Overshooting_Hermite_Cubic_Splines_For_Keyframe_Interpolation
        - https://en.wikipedia.org/w/index.php?title=Monotone_cubic_interpolation&oldid=950478742
        """
        pass


class BSplineInterpolator(_CubicInterpolator):
    """B-Spline Interpolator."""

    @staticmethod
    def interpolate(p0: float, p1: float, p2: float, p3: float, t: float) -> float:
        """Calculate the new point using the provided values."""
        pass


@functools.lru_cache(maxsize=10)
def _matrix_141(n: int) -> Matrix:
    """Get matrix '1 4 1'."""
    pass


class NaturalBSplineInterpolator(BSplineInterpolator):
    """Natural B-Spline interpolator."""

    DEF_END_COND = 'natural'

    @staticmethod
    def naturalize(points: list[Vector]) -> None:
        """
        Given a set of B-spline control points in the Nth dimension, create naturalized interpolation control points.

        Using the color points as `S0...Sn`, calculate `B0...Bn`, such that interpolation will
        pass through `S0...Sn`.

        When given 2 data points, the operation will be returned as linear, so there is nothing to do.
        """
        pass

    @classmethod
    def preprocess(cls, points: list[Vector], end_cond: str | None = None, **kwargs: Any) -> None:
        """Apply any preprocessing points."""
        pass


class SpragueInterpolator(Interpolator):
    """Sprague interpolator."""

    SPRAGUE_COEFFICIENTS = [
        [884, -1960, 3033, -2648, 1080, -180],
        [508, -540, 488, -367, 144, -24],
        [-24, 144, -367, 488, -540, 508],
        [-180, 1080, -2648, 3033, -1960, 884],
    ]

    @classmethod
    def preprocess(cls, points: list[Vector], **kwargs: Any) -> None:
        """Apply any preprocessing points."""
        pass

    def interpolate(self, p0: float, p1: float, p2: float, p3: float, p4: float, p5: float, t: float) -> float:
        """Interpolate with Sprague."""
        pass

    def run(self, i: int, t: float) -> Vector:
        """Begin interpolation."""
        pass


SPLINES = {
    'sprague': SpragueInterpolator,
    'natural': NaturalBSplineInterpolator,
    'bspline': BSplineInterpolator,
    'catrom': CatmullRomInterpolator,
    'monotone': MonotoneInterpolator,
    'linear': Interpolator
}  # type: dict[str, type[Interpolator]]


def interpolate(
    points: list[Vector] | Vector,
    domain: VectorLike | None = None,
    method: str = 'linear',
    extrapolate: bool = True,
    **kwargs: Any
) -> Interpolator:
    """Generic interpolation method."""
    pass


################################
# Matrix/linear algebra math
################################
def pretty(value: float | ArrayLike, *, _depth: int = 0, _shape: Shape | None = None) -> str:
    """Format the print output."""
    pass


def pprint(value: float | ArrayLike) -> None:
    """Print the matrix or value."""
    pass


def point_on_segment(a: VectorLike, b: VectorLike, p: VectorLike, abs_tol: float = ATOL) -> bool:
    """Point on line segment."""
    pass


def line_interesect(
    s1: VectorLike,
    e1: VectorLike,
    s2: VectorLike,
    e2: VectorLike,
    rel_tol: float = RTOL,
    abs_tol: float = ATOL
) -> Vector | None:
    """
    Find intersection of two lines.

    This was designed particularly for 3D intersection, but can be used for either 2D or 3D,
    but 2D line intersection could be calculated with less work using other methods if performance
    was of importance.

    3D lines rarely intersect, but often the shortest line between can be found.
    If the shortest line is has no length (a point) then it is an actual intersection.
    Our cases are constructed such that an intersection is expected, and a line is not sufficient.
    We can verify closeness of the points (to account for floating point errors) to verify that within
    some expected threshold, the two line points are essentially a point and an intersection is found.
    """
    pass


def all(a: float | ArrayLike) -> bool:  # noqa: A001
    """Return true if all elements are "true"."""
    pass


def any(a: float | ArrayLike) -> bool:  # noqa: A001
    """Return true if all elements are "true"."""
    pass


def vdot(a: VectorLike, b: VectorLike) -> float:
    """Dot two vectors."""
    pass


def vcross(v1: VectorLike, v2: VectorLike) -> Any:  # pragma: no cover
    """
    Cross two vectors.

    Takes vectors of either 2 or 3 dimensions. If 2 dimensions, will return the z component.
    To mix 2 and 3 vector components, please use `cross` instead which will pad 2 dimension
    vectors if the other is of 3 dimensions. `cross` has more overhead, so use `vcross` if
    you don't need broadcasting of any kind.
    """
    pass


@overload
def acopy(a: VectorLike) -> Vector:
    pass


@overload
def acopy(a: MatrixLike) -> Matrix:
    pass


@overload
def acopy(a: TensorLike) -> Tensor:
    pass


def acopy(a: ArrayLike) -> Array:
    """Array copy."""
    pass


@overload
def _cross_pad(a: VectorLike, s: ArrayShape) -> Vector:
    pass


@overload
def _cross_pad(a: MatrixLike, s: ArrayShape) -> Matrix:
    pass


@overload
def _cross_pad(a: TensorLike, s: ArrayShape) -> Tensor:
    pass


def _cross_pad(a: ArrayLike, s: ArrayShape) -> Array:
    """Pad an array with 2-D vectors."""
    pass


def cross(a: ArrayLike, b: ArrayLike) -> Any:
    """Vector cross product."""
    pass


def _extract_rows(m: ArrayLike, s: ArrayShape) -> Iterator[Vector]:
    """Extract row data from an array."""
    pass


def _extract_cols(m: ArrayLike, s: ArrayShape) -> Iterator[Vector]:
    """Extract column data from an array."""
    pass


@overload
def dot(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def dot(a: float, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot(a: VectorLike, b: float, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot(a: float, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def dot(a: MatrixLike, b: float, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def dot(a: float, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def dot(a: TensorLike, b: float, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def dot(a: VectorLike, b: VectorLike, *, dims: DimHints = ...) -> float:
    pass


@overload
def dot(a: VectorLike, b: MatrixLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot(a: MatrixLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot(a: VectorLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def dot(a: TensorLike, b: VectorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def dot(a: MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def dot(a: MatrixLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def dot(a: TensorLike, b: MatrixLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def dot(a: TensorLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


def dot(
    a: float | ArrayLike,
    b: float | ArrayLike,
    *,
    dims: DimHints = DN,
) -> float | Array:
    """
    Perform dot product.

    Operations involving scalars will be the same as calling `multiply`.

    If you are doing matrix multiplication, equivalent to `@` in `numpy`,
    then you want to use `matmul` instead. Operations on arrays of dimension 2
    or less will act the same as `matmul`.
    """
    pass


@overload
def matmul(a: VectorLike, b: VectorLike, *, dims: DimHints = ...) -> float:
    pass


@overload
def matmul(a: VectorLike, b: MatrixLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def matmul(a: MatrixLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def matmul(a: VectorLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def matmul(a: TensorLike, b: VectorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def matmul(a: MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def matmul(a: MatrixLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def matmul(a: TensorLike, b: MatrixLike, *, dims: DimHints = ...) -> Tensor | Matrix:
    pass


@overload
def matmul(a: TensorLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


def matmul(
    a: ArrayLike,
    b: ArrayLike,
    *,
    dims: DimHints = DN,
) -> float | Array:
    """
    Perform matrix multiplication of two arrays.

    Similar behavior as dot product, but this is limited to non-scalar values only. Additionally,
    the behavior of dimensions greater than 2 will be different. Stacks of matrices are broadcast
    together as if the matrices were elements, respecting the signature `(n,k),(k,m)->(n,m)`.
    This follows `numpy` behavior and is equivalent to the `@` operation.
    """
    pass


@overload
def matmul_x3(a: VectorLike, b: VectorLike, *, dims: DimHints = ...) -> float:
    pass


@overload
def matmul_x3(a: VectorLike, b: MatrixLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def matmul_x3(a: MatrixLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def matmul_x3(a: MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


def matmul_x3(
    a: MatrixLike | VectorLike,
    b: MatrixLike | VectorLike,
    *,
    dims: DimHints = DN,
) -> float | Vector | Matrix:
    """
    An optimized version of `matmul` that the total allowed dimensions to <= 2 and constrains dimensions lengths to 3.

    By limited to the total dimensions to < 2 and the dimension lengths of 3, loops are no longer required to handle
    an unknown number of dimensions or dimension lengths allowing for more optimized and faster performance at the
    cost of being able to handle any size arrays.

    For more flexibility with array sizes, use `matmul`.
    """
    pass


@overload
def dot_x3(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def dot_x3(a: float, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot_x3(a: VectorLike, b: float, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot_x3(a: float, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def dot_x3(a: MatrixLike, b: float, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def dot_x3(a: VectorLike, b: VectorLike, *, dims: DimHints = ...) -> float:
    pass


@overload
def dot_x3(a: VectorLike, b: MatrixLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot_x3(a: MatrixLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def dot_x3(a: MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


def dot_x3(
    a: MatrixLike | VectorLike | float,
    b: MatrixLike | VectorLike | float,
    dims: DimHints = DN
) -> float | Array:
    """
    An optimized version of `dot` that the total allowed dimensions to <= 2 and constrains dimensions lengths to 3.

    By limited to the total dimensions to < 2 and the dimension lengths of 3, loops are no longer required to handle
    an unknown number of dimensions or dimension lengths allowing for more optimized and faster performance at the
    cost of being able to handle any size arrays.

    For more flexibility with array sizes, use `dot`.
    """
    pass


def _matrix_chain_order(shapes: Sequence[ArrayShape]) -> MatrixInt:
    """
    Calculate chain order.

    Referenced the following sites:

    - https://en.wikipedia.org/wiki/Matrix_chain_multiplication
    - https://www.cs.cmu.edu/afs/cs/academic/class/15451-s04/www/Lectures/CRLS-DynamicProg.pdf

    This helped clarify `p` as that was not immediately clear:

    - https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

    We did adjust the looping. The algorithm originally called for looping from 2 - n,
    I can't see why though, so we've adjusted it to work from 1 - n.
    """
    pass


def _multi_dot(arrays: Sequence[ArrayLike], indexes: MatrixInt, i: int, j: int) -> ArrayLike:
    """Recursively dot the matrices in the array."""
    pass


def multi_dot(arrays: Sequence[ArrayLike]) -> Any:
    """
    Multi-dot.

    Dots matrices using the most efficient groupings to reduce operations.
    """
    pass


class _BroadcastTo:
    """
    Broadcast to a shape.

    By flattening the data, we are able to slice out the bits we need in the order we need
    and duplicate them to expand the matrix to fit the provided shape.

    We need 3 things to do this:
    - The original array.
    - The stage 1 array shape (with prepended 1s). This helps us calculate our loop iterations.
    - The new shape.
    """

    def __init__(self, array: ArrayLike | float, old: Shape, new: Shape) -> None:
        """Initialize."""
        pass

    def reset(self) -> None:
        """Reset."""
        pass

    def __next__(self) -> float:
        """Next."""
        pass

    def __iter__(self) -> Iterator[float]:
        """Return the broadcasted array, piece by piece."""
        pass


class _SimpleBroadcast:
    """
    Special broadcast of less than 2 arrays or 2 small dimension arrays that is faster than the generalized approach.

    A single array can have any dimensions, but two arrays must have dimensions less than 2.
    """

    def __init__(
        self,
        arrays: Sequence[ArrayLike | float],
        shapes: Sequence[Shape],
        new: Shape
    ) -> None:
        """Initialize."""
        pass

    def vector_broadcast(self, a: VectorLike, b: VectorLike) -> Iterator[tuple[float, ...]]:
        """Broadcast two vectors."""
        pass

    def broadcast(
        self,
        a: ArrayLike | float | None,
        b: ArrayLike | float | None,
        dims_a: int, dims_b: int
    ) -> Iterator[tuple[float, ...]]:
        """Simple broadcast of a single array or two arrays with dimensions less than 2."""
        pass

    def reset(self) -> None:
        """Reset."""
        pass

    def __next__(self) -> tuple[float, ...]:
        """Next."""
        pass

    def __iter__(self) -> Iterator[tuple[float, ...]]:  # pragma: no cover
        """Iterate."""
        pass


def _broadcast_shape(shapes: Sequence[Shape], max_dims: int, stage1_shapes: list[Shape] | None = None) -> Shape:
    """Find the common shape."""
    pass


class Broadcast:
    """Broadcast."""

    def __init__(self, *arrays: ArrayLike | float) -> None:
        """Broadcast."""
        pass

    def _init(self) -> None:
        """Setup main iterator."""
        pass

    def reset(self) -> None:
        """Reset iterator."""
        pass

    def __next__(self) -> tuple[float, ...]:
        """Next."""
        pass

    def __iter__(self) -> Broadcast:
        """Iterate."""
        pass


def broadcast(*arrays: ArrayLike | float) -> Broadcast:
    """Broadcast."""
    pass


@overload
def broadcast_to(a: ArrayLike | float, s: EmptyShape) -> float:
    pass


@overload
def broadcast_to(a: ArrayLike | float, s: int | VectorShape) -> Vector:
    pass


@overload
def broadcast_to(a: ArrayLike | float, s: MatrixShape) -> Matrix:
    pass


@overload
def broadcast_to(a: ArrayLike | float, s: TensorShape) -> Tensor:
    pass


def broadcast_to(a: ArrayLike | float, s: int | Shape) -> float | Array:
    """Broadcast array to a shape."""
    pass


class vectorize:
    """
    Vectorize a call.

    We do not currently support signatures, caching, and none of our functions allow specifying output
    types. All are assumed floats. Specialized methods will be far more performant than using vectorize,
    but vectorize can be quick to use as far as convenience is concerned.

    There is no optimization for small matrices or matrices that are already the same size. This
    assumes worst case: N x M matrices of unknown quantity.

    Inputs and outputs are currently assumed to be scalars. We do not detect alternate sizes nor
    do we allow specifying function signatures to change it at this time.
    """

    def __init__(
        self,
        pyfunc: Callable[..., Any],
        doc: str | None = None,
        excluded: Sequence[str | int] | None = None
    ) -> None:
        """Initialize."""
        pass

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call the function after once arguments are vectorized."""
        pass


class _vectorize1:
    """
    An optimized version of vectorize that is hard coded to broadcast only the first input.

    This is faster than `vectorize` as it skips a lot of generalization code that allows a user
    to specify specific parameters to broadcast. Additionally, users can specify `dims` allowing
    us to skip analyzing the array to determine the size allowing for additional speedup.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""
        pass

    def __call__(
        self,
        a: ArrayLike | float,
        dims: DimHints = DN,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""
        pass


class _vectorize2:
    """
    An optimized version of vectorize that is hard coded to broadcast only the first two inputs.

    This is faster than `vectorize` as it skips a lot of generalization code that allows a user
    to specify specific parameters to broadcast. Additionally, users can specify `dims` allowing
    us to skip analyzing the array to determine the size allowing for additional speedup.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""
        pass

    def _vector_apply(self, a: VectorLike, b: VectorLike, func: Callable[..., Any]) -> Any:
        """Apply a function to two vectors."""
        pass

    def __call__(
        self,
        a: ArrayLike | float,
        b: ArrayLike | float,
        dims: DimHints = DN,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""
        pass


class _vectorize1_x3:
    """
    A further optimized version of `_vectorize1` that limits arrays to dimensions of <= 2 and dimension to lengths of 3.

    Like `_vectorize1`, this limits the broadcasting to the first parameter and is faster than `vectorize` as it skips
    a lot of generalization code that allows a user to specify specific parameters to broadcast. Additionally, users
    can specify `dims` allowing us to skip analyzing the array to determine the size allowing for additional speedup.
    Lastly, dimensions are limited to a total less than 2 and the length of dimensions is limited to 3 which allows us
    to avoid looping since the dimension length is always the same.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""
        pass

    def __call__(
        self,
        a: ArrayLike | float,
        dims: DimHints = DN,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""
        pass


class _vectorize2_x3:
    """
    A further optimized version of `_vectorize2` that limits arrays to dimensions of <= 2 and dimension to lengths of 3.

    Like `_vectorize2`, this limits the broadcasting to the first two parameter and is faster than `vectorize` as it
    skips a lot of generalization code that allows a user to specify specific parameters to broadcast. Additionally,
    users can specify `dims` allowing us to skip analyzing the array to determine the size allowing for additional
    speedup. Lastly, dimensions are limited to a total less than 2 and the length of dimensions is limited to 3 which
    allows us to avoid looping since the dimension length is always the same.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """

    def __init__(self, pyfunc: Callable[..., Any], doc: str | None = None):
        """Initialize."""
        pass

    def __call__(
        self,
        a: MatrixLike | VectorLike | float,
        b: MatrixLike | VectorLike | float,
        dims: DimHints = DN,
        **kwargs: Any
    ) -> Any:
        """Call the vectorized function."""
        pass


def vectorize2(
    pyfunc: Callable[..., Any],
    doc: str | None = None,
    params: int = 2,
    only_x3: bool = False
) -> Callable[..., Any]:
    """
    A more limited but faster version of `vectorize` that speed up performance at the cost of flexibility.

    1. Broadcasted parameters are limited to the first 1 or 2 parameters via the `params` option (default 2).
    2. Further limits the expectation of the array in the first 1 or 2 parameters to dimension lengths of 3.
       Additionally, the total number of dimensions cannot exceed 2. `only_x3` enables this behavior and will
       provide the most speed but provides the most limited environment for operations.

    The limitations above allows the avoidance of additional generalized code that can slow the operation down.

    For more flexibility, use `vectorize` which allows arbitrary vectorization of any and
    all inputs at the cost of speed.
    """
    pass


@overload
def linspace(start: float, stop: float, num: int = ..., endpoint: bool = ...) -> Vector:
    pass


@overload
def linspace(start: VectorLike, stop: VectorLike | float, num: int = ..., endpoint: bool = ...) -> Matrix:
    pass


@overload
def linspace(start: VectorLike | float, stop: VectorLike, num: int = ..., endpoint: bool = ...) -> Matrix:
    pass


@overload
def linspace(start: MatrixLike, stop: ArrayLike, num: int = ..., endpoint: bool = ...) -> Tensor:
    pass


@overload
def linspace(start: ArrayLike, stop: MatrixLike, num: int = ..., endpoint: bool = ...) -> Tensor:
    pass


def linspace(start: ArrayLike | float, stop: ArrayLike | float, num: int = 50, endpoint: bool = True) -> Array:
    """Create a series of points in a linear space."""
    pass


def _isclose(a: float, b: float, *, equal_nan: bool = False, **kwargs: Any) -> bool:
    """Check if values are close."""
    pass


@overload  # type: ignore[no-overload-impl]
def isclose(a: float, b: float, *, dims: DimHints = ..., **kwargs: Any) -> bool:
    pass


@overload
def isclose(a: VectorLike, b: VectorLike, *, dims: DimHints = ..., **kwargs: Any) -> VectorBool:
    pass


@overload
def isclose(a: MatrixLike, b: MatrixLike, *, dims: DimHints = ..., **kwargs: Any) -> MatrixBool:
    pass


@overload
def isclose(a: TensorLike, b: TensorLike, *, dims: DimHints = ..., **kwargs: Any) -> TensorBool:
    pass


try:
    isclose = vectorize2(_isclose, doc="Test if a value or value(s) in an array are close to another value(s).")
except (NotImplementedError, TypeError, AttributeError):
    isclose = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def isnan(a: float, *, dims: DimHints = ..., **kwargs: Any) -> bool:
    pass


@overload
def isnan(a: VectorLike, *, dims: DimHints = ..., **kwargs: Any) -> VectorBool:
    pass


@overload
def isnan(a: MatrixLike, *, dims: DimHints = ..., **kwargs: Any) -> MatrixBool:
    pass


@overload
def isnan(a: TensorLike, *, dims: DimHints = ..., **kwargs: Any) -> TensorBool:
    pass


try:
    isnan = vectorize2(math.isnan, doc="Test if a value or values in an array are NaN.", params=1)
except (NotImplementedError, TypeError, AttributeError):
    isnan = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def sign(a: float, *, dims: DimHints = ..., **kwargs: Any) -> float:
    pass


@overload
def sign(a: VectorLike, *, dims: DimHints = ..., **kwargs: Any) -> Vector:
    pass


@overload
def sign(a: MatrixLike, *, dims: DimHints = ..., **kwargs: Any) -> Matrix:
    pass


@overload
def sign(a: TensorLike, *, dims: DimHints = ..., **kwargs: Any) -> Tensor:
    pass


try:
    sign = vectorize2(sgn, doc="Return the sign of a number.", params=1)
except (NotImplementedError, TypeError, AttributeError):
    sign = None  # type: ignore[assignment]


def prod(a: ArrayLike | float) -> float:
    """Return the product."""
    pass


def allclose(a: ArrayType, b: ArrayType, **kwargs: Any) -> bool:
    """Test if all are close."""
    pass


@overload  # type: ignore[no-overload-impl]
def multiply(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def multiply(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def multiply(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def multiply(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def multiply(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def multiply(a: TensorLike, b: float | ArrayLike, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def multiply(a: float | ArrayLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


try:
    multiply = vectorize2(operator.mul, doc="Multiply two arrays or floats.")
except (NotImplementedError, TypeError, AttributeError):
    multiply = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def divide(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def divide(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def divide(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def divide(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def divide(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def divide(a: TensorLike, b: float | ArrayLike, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def divide(a: float | ArrayLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


try:
    divide = vectorize2(operator.truediv, doc="Divide two arrays or floats.")
except (NotImplementedError, TypeError, AttributeError):
    divide = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def add(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def add(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def add(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def add(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def add(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def add(a: TensorLike, b: float | ArrayLike, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def add(a: float | ArrayLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass


try:
    add = vectorize2(operator.add, doc="Add two arrays or floats.")
except (NotImplementedError, TypeError, AttributeError):
    add = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def subtract(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def subtract(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def subtract(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def subtract(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def subtract(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def subtract(a: TensorLike, b: float | ArrayLike, *, dims: DimHints = ...) -> Tensor:
    pass


@overload
def subtract(a: float | ArrayLike, b: TensorLike, *, dims: DimHints = ...) -> Tensor:
    pass

try:
    subtract = vectorize2(operator.sub, doc="Subtract two arrays or floats.")
except (NotImplementedError, TypeError, AttributeError):
    subtract = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def multiply_x3(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def multiply_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def multiply_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def multiply_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def multiply_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


try:
    multiply_x3 = vectorize2(
        operator.mul,
        doc="Multiply two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
        only_x3=True
    )
except (NotImplementedError, TypeError, AttributeError):
    multiply_x3 = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def divide_x3(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def divide_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def divide_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def divide_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def divide_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


try:
    divide_x3 = vectorize2(
        operator.truediv,
        doc="Divide two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
        only_x3=True
    )
except (NotImplementedError, TypeError, AttributeError):
    divide_x3 = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def add_x3(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def add_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def add_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def add_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def add_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


try:
    add_x3 = vectorize2(
        operator.add,
        doc="Add two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
        only_x3=True
    )
except (NotImplementedError, TypeError, AttributeError):
    add_x3 = None  # type: ignore[assignment]


@overload  # type: ignore[no-overload-impl]
def subtract_x3(a: float, b: float, *, dims: DimHints = ...) -> float:
    pass


@overload
def subtract_x3(a: float | VectorLike, b: VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def subtract_x3(a: VectorLike, b: float | VectorLike, *, dims: DimHints = ...) -> Vector:
    pass


@overload
def subtract_x3(a: MatrixLike, b: float | VectorLike | MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


@overload
def subtract_x3(a: float | VectorLike | MatrixLike, b: MatrixLike, *, dims: DimHints = ...) -> Matrix:
    pass


try:
    subtract_x3 = vectorize2(
        operator.sub,
        doc="Subtract two arrays or floats.\n\nOptimized for scalars, dimensions <= 2, and vectors of lengths of 3.",
        only_x3=True
    )
except (NotImplementedError, TypeError, AttributeError):
    subtract_x3 = None  # type: ignore[assignment]


@overload
def full(array_shape: EmptyShape, fill_value: float | ArrayLike) -> float:
    pass

@overload
def full(array_shape: int | VectorShape, fill_value: float | ArrayLike) -> Vector:
    pass


@overload
def full(array_shape: MatrixShape, fill_value: float | ArrayLike) -> Matrix:
    pass


@overload
def full(array_shape: TensorShape, fill_value: float | ArrayLike) -> Tensor:
    pass


def full(array_shape: int | Shape, fill_value: float | ArrayLike) -> Array | float:
    """Create and fill a shape with the given values."""
    pass


@overload
def ones(array_shape: EmptyShape) -> float:
    pass


@overload
def ones(array_shape: int | VectorShape) -> Vector:
    pass


@overload
def ones(array_shape: MatrixShape) -> Matrix:
    pass


@overload
def ones(array_shape: TensorShape) -> Tensor:
    pass


def ones(array_shape: int | Shape) -> Array | float:
    """Create and fill a shape with ones."""
    pass


@overload
def zeros(array_shape: EmptyShape) -> float:
    pass

@overload
def zeros(array_shape: int | VectorShape) -> Vector:
    pass


@overload
def zeros(array_shape: MatrixShape) -> Matrix:
    pass


@overload
def zeros(array_shape: TensorShape) -> Tensor:
    pass


def zeros(array_shape: int | Shape) -> Array | float:
    """Create and fill a shape with zeros."""
    pass


def ndindex(*s: Shape) -> Iterator[tuple[int, ...]]:
    """Iterate dimensions."""
    pass


def ndenumerate(a: ArrayLike | float) -> Iterator[tuple[Shape, Any]]:
    """Iterate dimensions."""
    pass


class ArrayBuilder:
    """Auto drain an iterator."""

    def __init__(self, a: Array, s: Shape) -> None:
        """Initialize."""
        pass

    def __enter__(self) -> Iterator[Any]:
        """Enter."""
        pass

    def __exit__(self: Any, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """Drain the iterator."""
        pass

    @staticmethod
    def _new_array_builder(a: Array, s: Shape) -> Iterator[Any]:
        """Generate a new array based on the specified size returning each row for appending."""
        pass


class MultiArrayBuilder(ArrayBuilder):
    """Auto drain an iterator."""

    def __init__(self, a: Sequence[Array], s: Sequence[Shape]) -> None:
        """Initialize."""
        pass

    def __enter__(self) -> list[Iterator[Any]]:  # type: ignore[override]
        """Enter."""
        pass

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """Drain the iterator."""
        pass


def flatiter(array: float | ArrayLike) -> Iterator[float]:
    """Traverse an array returning values."""
    pass


def ravel(array: float | ArrayLike) -> Vector:
    """Return a flattened vector."""
    pass


def _frange(start: float, stop: float, step: float) -> Iterator[float]:
    """Float range."""
    pass


def arange(
    start: SupportsFloatOrInt,
    stop: SupportsFloatOrInt | None = None,
    step: SupportsFloatOrInt = 1
) -> Vector:
    """
    Like arrange, but handles floats as well.

    Return will be a list instead of an iterator.
    Due to floating point precision, floats may be inaccurate to some degree.
    """
    pass


@overload
def transpose(array: float) -> float:
    pass


@overload
def transpose(array: VectorLike) -> Vector:
    pass


@overload
def transpose(array: MatrixLike) -> Matrix:
    pass


@overload
def transpose(array: TensorLike) -> Tensor:
    pass


def transpose(array: ArrayLike | float) -> float | Array:
    """
    A simple transpose of a matrix.

    `numpy` offers the ability to specify different axes, but right now,
    we don't have a need for that, nor the desire to figure it out :).
    """
    pass


@overload
def reshape(array: ArrayLike | float, new_shape: EmptyShape) -> float:
    pass


@overload
def reshape(array: ArrayLike | float, new_shape: int | VectorShape) -> Vector:
    pass


@overload
def reshape(array: ArrayLike | float, new_shape: MatrixShape) -> Matrix:
    pass


@overload
def reshape(array: ArrayLike | float, new_shape: TensorShape) -> Tensor:
    pass


def reshape(array: ArrayLike | float, new_shape: int | Shape) -> float | Array:
    """Change the shape of an array."""
    pass


@overload
def _quick_shape(a: float) -> EmptyShape:
    pass


@overload
def _quick_shape(a: VectorLike) -> VectorShape:
    pass


@overload
def _quick_shape(a: MatrixLike) -> MatrixShape:
    pass


@overload
def _quick_shape(a: TensorLike) -> TensorShape:
    pass


def _quick_shape(a: ArrayLike | float) -> Shape:
    """
    Acquire shape taking shortcuts by assuming a non-ragged, consistently shaped array.

    No checking for consistency is performed allowing for a quicker check.
    """
    pass


@overload
def shape(a: float) -> EmptyShape:
    pass


@overload
def shape(a: VectorLike) -> VectorShape:
    pass


@overload
def shape(a: MatrixLike) -> MatrixShape:
    pass


@overload
def shape(a: TensorLike) -> TensorShape:
    pass


def shape(a: ArrayLike | float) -> Shape:
    """Get the shape of a list."""
    pass


def fill_diagonal(matrix: Matrix | Tensor, val: float | ArrayLike, wrap: bool = False) -> None:
    """Fill an N-D matrix diagonal."""
    pass


def eye(n: int, m: int | None = None, k: int = 0) -> Matrix:
    """Create a diagonal of ones in a zero initialized matrix at the specified position."""
    pass


def identity(size: int) -> Matrix:
    """Create an identity matrix."""
    pass


@overload
def diag(array: VectorLike, k: int = ...) -> Matrix:
    pass


@overload
def diag(array: MatrixLike, k: int = ...) -> Vector:
    pass


def diag(array: VectorLike | MatrixLike, k: int = 0) -> Vector | Matrix:
    """Create a diagonal matrix from a vector or return a vector of the diagonal of a matrix."""
    pass


def lu(
    matrix: MatrixLike | TensorLike,
    *,
    permute_l: bool = False,
    p_indices: bool = False,
    _shape: Shape | None = None
) ->  Any:
    """
    Calculate `LU` decomposition.

    P is returned as `PA = UL` or `A = P'UL` which follows `Matlab` and `Octave` opposed to `Scipy` which returns P as
    `A = PUL` or `P'A = UL`. For matrix inverse, we need P such that `PA = UL` and it is faster not having to invert
    P, even if we can invert it fairly fast as it is just a shuffled identity matrix.

    P is returned as a permutation matrix unless `p_indices` is true, in which case `P` would be returned as
    a vector containing the indexes such that `A[P,:] = L*U`.

    If `permute_l` is true, only L and U will be returned such that `P = LU`.

    Reference: https://www.statlect.com/matrix-algebra/Gaussian-elimination
               https://www.sciencedirect.com/topics/mathematics/partial-pivoting
    """
    pass


def _forward_sub_vector(a: Matrix, b: Vector, size: int) -> Vector:
    """Forward substitution for solution of `L x = b`."""
    pass


def _forward_sub_matrix(a: Matrix, b: Matrix, s: ArrayShape) -> Matrix:
    """Forward substitution for solution of `L x = b` where `b` is a matrix."""
    pass


def _back_sub_vector(a: Matrix, b: Vector, size: int) -> Vector:
    """Back substitution for solution of `U x = b`."""
    pass


def _back_sub_matrix(a: Matrix, b: Matrix, s: ArrayShape) -> Matrix:
    """Back substitution for solution of `U x = b`."""
    pass


def _householder_reduction_bidiagonal(
    m: int,
    n: int,
    e: Vector,
    u: Matrix,
    q: Vector,
    tol: float
) -> tuple[float, int, float, float]:
    """Householder's reduction to bidiagonal form."""
    pass


def _accumulate_right_transfrom(n: int, g: float, l: int, e: Vector, u: Matrix, v: Matrix) -> float:
    """Accumulation of right hand transformations."""
    pass


def _accumulate_left_transform(m: int, n: int, g: float, l: int, u: Matrix, q: Vector) -> float:
    """Accumulation of left hand transformations."""
    pass


def _compute_orthogonal_rotation(a: float, b: float) -> tuple[float, float, float]:
    """Compute orthogonal rotation avoiding divide by zero."""
    pass


def _diagonalization_of_bidiagonal(
    m: int,
    n: int,
    g: float,
    x: float,
    y: float,
    e: Vector,
    u: Matrix,
    q: Vector,
    v: Matrix,
    eps: float
) -> None:
    """Diagonalization of the bidiagonal form."""
    pass


def _svd(a: MatrixLike, m: int, n: int, full_matrices: bool = True, compute_uv: bool = True) -> Any:
    """
    Compute the singular value decomposition of a matrix.

    Handbook Series Linear Algebra
    Singular Value Decomposition and Least Squares Solutions
    G. H. Golub and C. Reinsch
    https://people.duke.edu/~hpgavin/SystemID/References/Golub+Reinsch-NM-1970.pdf

    Some small changes were made to support wide and tall matrices. Additionally,
    we fixed some cases where divide by zero could occur and confirmed that the
    solutions still yielded `A = U∑V^T`.
    """
    pass


def svd(
    a: MatrixLike | TensorLike,
    full_matrices: bool = True,
    compute_uv: bool = True
) -> Any:
    """
    Compute the singular value decomposition of a matrix.

    This differs from Numpy in that it returns `U, S, V` instead of `U, S, V^T`.

    There are far more efficient and modern algorithms than what we have implemented here.
    This approach is not recommended for very large matrices as it will be too slow. While
    it is sufficient for computing smaller matrices, it is not practical for very large
    matrices, such as compressing images with thousands of pixels. If you are doing serious
    computations with very large matrices, Numpy or SciPy should be strongly considered.
    """
    pass


def svdvals(a: MatrixLike | TensorLike) -> Any:
    """Get the s values from SVD."""
    pass


def _qr(a: Matrix, m: int, n: int, mode: str = 'reduced') -> Any:
    """Perform QR decomposition on a matrix."""
    pass


def qr(
    a: MatrixLike | TensorLike,
    mode: str = 'reduced'
) -> Any:
    """
    QR decomposition using householder reflections.

    https://www.cs.cornell.edu/~bindel/class/cs6210-f09/lec18.pdf

    Generally this provides a similar interface to Numpy with the following modes:

    - "reduced": returns Q, R with dimensions `(…, M, K)`, `(…, K, N)`
    - "complete": returns Q, R with dimensions `(…, M, M)`, `(…, M, N)`
    - "r": returns R only with dimensions `(…, K, N)`
    - "raw": returns h, tau with dimensions `(…, N, M)`, `(…, K,)` where
      h is the R matrix with the householder reflections in the lower triangle.
      Unlike Numpy, we do not provide the transposed matrix for Fortran.
    """
    pass


def matrix_rank(a: MatrixLike | TensorLike) -> Any:
    """Calculate the matrix rank."""
    pass


@overload
def solve(a: MatrixLike, b: VectorLike) -> Vector:
    pass


@overload
def solve(a: MatrixLike, b: MatrixLike) -> Matrix:
    pass


@overload
def solve(a: MatrixLike, b: TensorLike) -> Tensor:
    pass


@overload
def solve(a: TensorLike, b: VectorLike) -> Matrix | Tensor:
    pass


@overload
def solve(a: TensorLike, b: MatrixLike | TensorLike) -> Tensor:
    pass


def solve(a: MatrixLike | TensorLike, b: ArrayLike) -> Array:
    """
    Solve the system of equations for `x` where `ax = b`.

    Normal broadcasting applies and the behavior matches Numpy 2+.
    """
    pass


def trace(matrix: Matrix) -> float:
    """Sum the diagonal."""
    pass


@overload
def det(array: MatrixLike) -> float:
    pass


@overload
def det(array: TensorLike) -> Vector:
    pass


def det(array: MatrixLike | TensorLike) -> float | Vector:
    """Get the determinant."""
    pass


@overload
def inv(matrix: MatrixLike) -> Matrix:
    pass


@overload
def inv(matrix: TensorLike) -> Tensor:
    pass


def inv(matrix: MatrixLike | TensorLike) -> Matrix | Tensor:
    """Invert the matrix using `LU` decomposition."""
    pass


@overload
def pinv(a: MatrixLike) -> Matrix:
    pass


@overload
def pinv(a: TensorLike) -> Tensor:
    pass


def pinv(a: MatrixLike | TensorLike) -> Matrix | Tensor:
    """
    Compute the (Moore-Penrose) pseudo-inverse of a matrix using SVD.

    Negative results can be returned, use `fnnls` for a non-negative solution (if possible).
    """
    pass


@overload
def vstack(arrays: Sequence[float | Vector | Matrix]) -> Matrix:
    pass


@overload
def vstack(arrays: Sequence[Tensor]) -> Tensor:
    pass


def vstack(arrays: Sequence[ArrayLike | float]) -> Matrix | Tensor:
    """Vertical stack."""
    pass


def _hstack_extract(a: ArrayLike | float, s: ArrayShape) -> Iterator[Array]:
    """Extract data from the second axis."""
    pass


def hstack(arrays: Sequence[ArrayLike | float]) -> Array:
    """Horizontal stack."""
    pass


def outer(a: float | ArrayLike, b: float | ArrayLike) -> Matrix:
    """Compute the outer product of two vectors (or flattened matrices)."""
    pass


@overload
def inner(a: float, b: float) -> float:
    pass


@overload
def inner(a: float, b: VectorLike) -> Vector:
    pass


@overload
def inner(a: VectorLike, b: float) -> Vector:
    pass


@overload
def inner(a: float, b: MatrixLike) -> Matrix:
    pass


@overload
def inner(a: MatrixLike, b: float) -> Matrix:
    pass


@overload
def inner(a: float, b: TensorLike) -> Tensor:
    pass


@overload
def inner(a: TensorLike, b: float) -> Tensor:
    pass


@overload
def inner(a: VectorLike, b: VectorLike) -> float:
    pass


@overload
def inner(a: VectorLike, b: MatrixLike) -> Vector:
    pass


@overload
def inner(a: MatrixLike, b: VectorLike) -> Vector:
    pass


@overload
def inner(a: VectorLike, b: TensorLike) -> Tensor | Matrix:
    pass


@overload
def inner(a: TensorLike, b: VectorLike) -> Tensor | Matrix:
    pass


@overload
def inner(a: MatrixLike, b: MatrixLike) -> Matrix:
    pass


@overload
def inner(a: MatrixLike, b: TensorLike) -> Tensor | Matrix:
    pass


@overload
def inner(a: TensorLike, b: MatrixLike) -> Tensor | Matrix:
    pass


@overload
def inner(a: TensorLike, b: TensorLike) -> Tensor:
    pass


def inner(a: float | ArrayLike, b: float | ArrayLike) -> float | Array:
    """Compute the inner product of two arrays."""
    pass


def fnnls(
    A: MatrixLike,
    b: VectorLike,
    epsilon: float = ATOL,
    max_iters: int = 0
) -> tuple[Vector, float]:
    """
    Fast non-negative least squares.

    A fast non-negativity-constrained least squares
    https://www.researchgate.net/publication/230554373_A_Fast_Non-negativity-constrained_Least_Squares_Algorithm
    Rasmus Bro and Sijmen De Jong
    Journal of Chemometrics. 11, 393-401 (1997)
    """
    pass


@overload
def flip(a: float, axis: int | tuple[int, ...] | None = ...) -> float:
    pass


@overload
def flip(a: VectorLike, axis: int | tuple[int, ...] | None = ...) -> Vector:
    pass


@overload
def flip(a: MatrixLike, axis: int | tuple[int, ...] | None = ...) -> Matrix:
    pass


@overload
def flip(a: TensorLike, axis: int | tuple[int, ...] | None = ...) -> Tensor:
    pass


def flip(a: ArrayLike | float, axis: int | tuple[int, ...] | None = None) -> Array | float:
    """Flip specified axis/axes."""
    pass


@overload
def flipud(a: float) -> float:
    pass


@overload
def flipud(a: VectorLike) -> Vector:
    pass


@overload
def flipud(a: MatrixLike) -> Matrix:
    pass


@overload
def flipud(a: TensorLike) -> Tensor:
    pass


def flipud(a: ArrayLike | float) -> Array | float:
    """Flip axis 0."""
    pass


@overload
def fliplr(a: float) -> float:
    pass


@overload
def fliplr(a: VectorLike) -> Vector:
    pass


@overload
def fliplr(a: MatrixLike) -> Matrix:
    pass


@overload
def fliplr(a: TensorLike) -> Tensor:
    pass


def fliplr(a: ArrayLike | float) -> Array | float:
    """Flip axis 1."""
    pass


@overload
def roll(a: float, shift: int | tuple[int, ...], axis: int | tuple[int, ...] | None = ...) -> float:
    pass


@overload
def roll(a: VectorLike, shift: int | tuple[int, ...], axis: int | tuple[int, ...] | None = ...) -> Vector:
    pass


@overload
def roll(a: MatrixLike, shift: int | tuple[int, ...], axis: int | tuple[int, ...] | None = ...) -> Matrix:
    pass


@overload
def roll(a: TensorLike, shift: int | tuple[int, ...], axis: int | tuple[int, ...] | None = ...) -> Tensor:
    pass


def roll(
    a: ArrayLike | float,
    shift: int | tuple[int, ...],
    axis: int | tuple[int, ...] | None = None
) -> Array | float:
    """Roll specified axis/axes."""
    pass


def unique(
    a: ArrayLike | float,
    axis: int | None = None,
    return_index: bool = False,
    return_inverse: bool = False,
    return_counts: bool = False
) -> Any:
    """Return unique elements."""
    pass
