import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib import style


def function(equation, root, start, stop) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.plot([i for i in np.arange(start, stop, 0.01)], [equation(i) for i in np.arange(start, stop, 0.01)])
    if root is not None:
        ax.plot(root, equation(root), 'o')
    ax.set_title(f"Root in [{start},{stop}]")
    ax.grid(True)
    plt.show()


def system(equation1, equation2):
    style.use('ggplot')
    x, y = sp.symbols("x y")
    sp.plot_implicit(sp.Or(sp.Eq(equation1(x, y), 0), sp.Eq(
        equation2(x, y), 0)))
