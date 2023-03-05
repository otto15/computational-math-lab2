from math import *
from typing import Callable
from data.equations import equations

derivatives_of_equations: dict[Callable[[float], float], Callable[[float], float]] = {
    equations[0]: lambda x: 3 * x ** 2 - 1,
    equations[1]: lambda x: -4 * sin(2 * x) + 3 * cos(x),
    equations[2]: lambda x: 12 * x ** 2 + 40 * x,
}


def derivative(f: Callable[[float], float]) -> Callable[[float], float]:
    return derivatives_of_equations[f]
