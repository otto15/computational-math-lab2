from typing import Callable

from utils import OutputData


def solve(f: Callable[[float], float], start: float, stop: float, epsilon: float) -> OutputData:
    if f(start) * f(stop) > 0:
        print("There is no root or more than one")
        return None

    x = start
    i = 0
    while abs(start - stop) > epsilon and abs(f(x)) >= epsilon:
        x = (start + stop) / 2
        if f(start) * f(x) > 0:
            start = x
        else:
            stop = x
        i += 1
    x = (start + stop) / 2
    return OutputData(x, f(x), i)
