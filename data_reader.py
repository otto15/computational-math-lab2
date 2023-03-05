import re
from pathlib import Path
from typing import Callable
from data.equations import equation_views, equations, system_of_equations_views, systems_of_equations


class InputData:
    equation: Callable[[float], float]
    method: int
    system_of_equations: tuple[Callable[[float], float]] = None
    interval: list[float]
    accuracy: float
    x0: float
    y0: float


def input_choice(choices: set, msg: str) -> int:
    choice: int
    while True:
        try:
            choice = int(input(msg))
            if choice not in choices:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice, try again...")


def choose_single_equation() -> Callable[[float], float]:
    for i in range(len(equation_views)):
        print(f'{i + 1}. {equation_views[i]}')
    eq_choice: int = input_choice(set(range(1, len(equation_views) + 1)), "Type a number of the desired equation: ")
    return equations[eq_choice - 1]


def choose_single_system_of_equations() -> list[Callable[[float], float]]:
    for i in range(len(system_of_equations_views)):
        print(f'{i + 1}. {system_of_equations_views[i]}')
    eq_choice: int = input_choice(set(range(1, len(system_of_equations_views) + 1)),
                                  "Type a number of the desired system of equations: ")
    return systems_of_equations[eq_choice - 1]


def input_data() -> InputData:
    data: InputData = InputData()
    eq_type: int = input_choice({1, 2}, 'Type "1" if you want to choose a single equation, "2" - system of equations: ')
    match eq_type:
        case 1:
            data.equation = choose_single_equation()
            data.method = input_choice({1, 2, 3}, "1. half division\n2. secant\n3. simple iterations\nChoose method: ")
            input_source: int = input_choice({1, 2},
                                             'Type "1" if you want to use console as source of interval and accuracy, '
                                             '"2" - file: ')
            match input_source:
                case 1:
                    data.interval = input_interval()
                    data.accuracy = input_accuracy()
                case 2:
                    data.interval, data.accuracy = input_data_from_file()
        case 2:
            data.system_of_equations = choose_single_system_of_equations()
            data.x0, data.y0 = input_approx()

    return data


def input_interval() -> list[float]:
    while True:
        try:
            start: float = float(input("Type start of the interval: "))
            break
        except ValueError:
            print("Invalid input, try again... ")

    while True:
        try:
            end = float(input("Type end of the interval: "))
            if end <= start:
                print("End must be greater than start, try again...")
                continue
            break
        except ValueError:
            print("Invalid input, try again... ")

    return [start, end]


def input_approx() -> list[float]:
    x0: float
    while True:
        try:
            x0 = float(input("Type x approximation: "))
            break
        except ValueError:
            print("Invalid x approximation, try again")
    y0: float
    while True:
        try:
            y0 = float(input("Type y approximation: "))
            break
        except ValueError:
            print("Invalid y approximation, try again")
    return [x0, y0]


def input_accuracy() -> float:
    while True:
        try:
            accuracy: float = float(input("Type accuracy: "))
            if accuracy <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid accuracy, try again")

    return accuracy


def input_data_from_file() -> list[list[float], float]:
    filename: str = input("Type file name: ")
    while not Path(filename).is_file():
        filename: str = input("No such file, try again: ")
    with open(filename, "r") as f:
        data: str = f.read()

        try:
            content: list[float] = list(map(float, data.split()))
        except ValueError:
            raise ValueError("Invalid argument types in file")

    if len(content) != 3:
        raise ValueError("Invalid number of arguments in file")

    if content[1] < content[0]:
        ValueError("End of the interval must be greater than start")

    if content[2] <= 0:
        ValueError("Accuracy must be positive")

    return [[content[0], content[1]], content[2]]
