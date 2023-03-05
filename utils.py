class OutputData:
    x: float
    func_val: float
    iter_number: int
    errors: list[list[float]]
    roots: list[float]

    def __init__(self, x: float, func_val: float, iter_number: int):
        self.x = x
        self.func_val = func_val
        self.iter_number = iter_number
