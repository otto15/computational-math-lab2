from derivatives import derivative
from typing import Callable


def find_root_simple_iteration(f: Callable[[float], float], start: float, stop: float, epsilon: float) -> float:
    print("__________________simple iteration__________________")
    l: float = find_lambda(f, start, stop)
    q: float = find_q(lambda x: 1 + l * derivative(f)(x), start, stop)

    print(f"lambda={round(l, 5)}, q=={round(q, 5)}")

    phi: Callable[[float], float] = lambda x: x + f(x) * l
    print(f"phi(x) = x + f(x)*{round(l, 5)}")

    if q > 0.5:
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) > epsilon
    else:
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) >= (1 - q / q) * epsilon

    x0: float = start
    x1: float = phi(x0)

    xi: float = x1
    xi_prev: float = x0

    while (check(epsilon, xi, xi_prev, q)):
        tmp = xi
        xi = phi(xi)
        xi_prev = tmp
    print("__________________simple iteration end__________________")

    return xi


def find_lambda(f: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(derivative(f)(start))
    while start < stop:
        if max_derivative < abs(derivative(f)(start)):
            max_derivative = abs(derivative(f)(start))
        start += 0.01
    return -1 / max_derivative


def find_q(f: Callable[[float], float], start: float, stop: float):
    max_derivative = abs(f(start))
    while start < stop:
        if max_derivative < abs(f(start)):
            max_derivative = abs(f(start))
        start += 0.01
    return max_derivative
