from typing import Callable

from utils import OutputData


def d(n, x, f, h=0.00000001):
    if n <= 0:
        return None
    elif n == 1:
        return (f(x + h) - f(x)) / h

    return (d(n - 1, x + h, f) - d(n - 1, x, f)) / h


def solve(equation: Callable[[float], float], interval: list[float], accuracy: float) -> OutputData:
    if equation(interval[0]) * equation(interval[1]) > 0:
        print("There is no root or more than one")
        return None

    previous_x: float

    if equation(interval[0]) * d(2, interval[0], equation) > 0:
        previous_x = interval[0]
    elif equation(interval[1]) * d(2, interval[1], equation) > 0:
        previous_x = interval[1]
    else:
        print("Sorry, but sufficient condition is not met: signs of derivatives are not equal for both start and end "
              "of interval")
        return None

    current_x: float = previous_x + 0.03

    next_x: float = current_x - equation(current_x) * (current_x - previous_x) / (
                equation(current_x) - equation(previous_x))

    current_iteration: int = 1
    max_iteration: int = 100000

    while abs(next_x - current_x) > accuracy and current_iteration < max_iteration:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - equation(current_x) * (current_x - previous_x) / (
                    equation(current_x) - equation(previous_x))

        current_iteration += 1

    if current_iteration == max_iteration or (next_x > interval[1] or next_x < interval[0]):
        print("No roots on given interval")
        return None

    return OutputData(next_x, equation(next_x), current_iteration)
