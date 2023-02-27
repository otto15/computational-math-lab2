from typing import Callable

equations: list[Callable[[float], float]] = [
    lambda x: 45 * x ** 3 - 91 * x ** 2 + x + 123
]