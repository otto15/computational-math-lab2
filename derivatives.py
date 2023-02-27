from math import *
from typing import Callable
from resource import equations

derivatives: dict[Callable[[float], float], Callable[[float], float]] = {
    equations[0]: lambda x: 135 * x ** 2 - 182 * x + 1,
}


def derivative(f: Callable[[float], float]) -> Callable[[float], float]:
    return derivatives[f]
