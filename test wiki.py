# для проверки функций
from math import sin, cos
from typing import Callable
import unittest
from funcs import *


def field(divisions, first, last):
    _h = (first - last) / divisions
    _field = []
    for _ in range(divisions + 1):
        _field.append(first + _ * _h)
    return _field, _h

def newton(f: Callable[[float], float], f_prime: Callable, dimension,
           eps: float = 1e-7, kmax: int = 1e3) -> float:
    """
    solves f(x) = 0 by Newton's method with precision eps
    :param dimension:
    :param kmax:
    :param f: f
    :param f_prime: f'
    # :param x0: starting point
    :param eps: precision wanted
    :return: root of f(x) = 0
    """
    _field, _h = dimension
    x0 = _field[0]
    x, x_prev, i = x0, x0 + 2 * eps, 0

    while abs(x - x_prev) >= eps and i < kmax:
        x, x_prev, i = x - f(x) / f_prime(x, _h), x, i + 1

    return x

print(newton(y, f1_center, field(100, -10, 10)))
