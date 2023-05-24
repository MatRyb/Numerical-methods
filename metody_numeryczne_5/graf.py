import matplotlib.pyplot as plt
from sympy import *
import numpy as np

from cheb_poly import Approximation


def graf_print(a, b, funct, n, nodes):
    x = Symbol('x')
    aprox = Approximation(funct, n, nodes)
    x_aprox = np.linspace(a, b, 100)
    y_aprox = [aprox.subs(x, i) for i in x_aprox]
    y_real = [funct.subs(x, i) for i in x_aprox]
    plt.figure(figsize=(10, 7))
    plt.plot(x_aprox, y_real, color='blue', label='funkcja aproksymowana')
    plt.plot(x_aprox, y_aprox, color='lime', label='funkcja aproksymacyjna',linestyle='--')

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    plt.show()