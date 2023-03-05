from typing import Callable
from data.jacobians import jacobians
from methods import gauss


def solve(system: tuple[Callable[[float, float], float]], x0: float, y0: float):
    matrix: list[list[float]]
    errors: list[list[float]] = [[], []]
    i: int = 0
    epsilon: float = 0.01
    inc_x, inc_y = epsilon + 1, epsilon + 1
    while abs(inc_x) > epsilon or abs(inc_y) > epsilon:
        matrix = []
        for j in range(len(jacobians[system])):
            ls = jacobians[system][j]
            matrix.append([])
            matrix[-1].append(ls[0](x0))
            matrix[-1].append(ls[1](y0))
            matrix[-1].append(-system[j](x0, y0))

        inc_x, inc_y = gauss.count_result(matrix)
        errors[0].append(inc_x)
        errors[1].append(inc_y)
        x0 += inc_x
        y0 += inc_y
        i += 1

    print(f'Solution: [{round(x0, 5), round(y0, 5)}]')
    print(f'Pogreshnosty for x: {errors[0]}')
    print(f'Pogreshnosty for y: {errors[1]}')
    print(f'Number of iterations: {i}')
