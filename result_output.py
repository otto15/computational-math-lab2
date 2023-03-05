from pathlib import Path

from data_reader import input_choice


def output_results(x: float, func_val: float, iter_number: int) -> None:
    input_source: int = input_choice({1, 2}, 'Type "1" if you want to print results in console, "2" - in file: ')

    match input_source:
        case 1:
            print(f'x = {round(x, 5)}, f(x) = {round(func_val, 5)}, number of iterations = {iter_number}')
        case 2:
            output_to_file(x, func_val, iter_number)


def output_to_file(x: float, func_val: float, iter_number: int) -> None:
    filename: str = input("Type file name: ")
    while not Path(filename).is_file():
        filename: str = input("No such file, try again: ")
    with open(filename, "w") as f:
        print(f'x = {round(x, 5)}, f(x) = {round(func_val, 5)}, number of iterations = {iter_number}', file=f)
