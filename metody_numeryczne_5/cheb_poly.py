import numpy as np
from sympy import *
import Cheby_gauss
import math as ma


def Cheby_poly(n):
    x = Symbol('x')
    poly_list = [cos(i * acos(x)) for i in range(2)]
    for i in range(2, n):
        poly_list.append(simplify(2 * x * poly_list[i - 1] - poly_list[i - 2]))
    return poly_list


def Approximation(funct, n, nodes):
    x = Symbol('x')
    T_k = Cheby_poly(n)
    result = simplify(x - x)
    for i in range(n):
        count = simplify(funct * T_k[i])
        integral = Cheby_gauss.Cheby_Gauss_function(count, nodes)
        if i == 0:
            result_integral = integral / ma.pi
        else:
            result_integral = integral / (ma.pi / 2)

        result += simplify(result_integral * T_k[i])
    return result


def error_approx(a, b, funct, n, nodes):
    x = Symbol('x')
    y_x = Approximation(funct, n, nodes)
    sum = simplify(x - x)
    points = np.linspace(a, b, n)
    for i in points:
        sum += (funct.subs(x, i) - y_x.subs(x, i)) ** 2
    result = sqrt(sum)
    return result
