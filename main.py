from data_reader import input_data
from methods import simple_iteration, secant, half_division
import plot
from utils import OutputData
from result_output import output_results
from methods import newton

if __name__ == '__main__':
    try:
        data = input_data()

        if data.system_of_equations is not None:
            newton.solve(data.system_of_equations, data.x0, data.y0)
            plot.system(data.system_of_equations[0], data.system_of_equations[1])
        else:
            result: OutputData = None
            match data.method:
                case 1:
                    result = half_division.solve(data.equation, data.interval[0], data.interval[1], data.accuracy)
                case 2:
                    result = secant.solve(data.equation, data.interval, data.accuracy)
                case 3:
                    result = simple_iteration.solve(data.equation, data.interval[0], data.interval[1], data.accuracy)
            if result is not None:
                output_results(result.x, result.func_val, result.iter_number)
                plot.function(data.equation, result.x, data.interval[0], data.interval[1])
            else:
                plot.function(data.equation, None, data.interval[0], data.interval[1])
    except ValueError as e:
        print(str(e))
    except (EOFError, KeyboardInterrupt):
        print("Something bad happened...")
