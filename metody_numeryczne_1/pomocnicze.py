import numpy as np
import matplotlib.pyplot as plt

import pomocnicze


def sin_function(x):
    return np.sin(x)


def cos_function(x):
    return np.cos(x)


def tg_function(x):
    return np.tan(x)


def ctg_function(x):
    return 1 / np.tan(x)


def horner(value, polynomial) -> float:
    result_horner = 0

    for i in polynomial:
         result_horner = result_horner * value + i

    return result_horner


def trygonemetric_function(x):
    return 2*sin_function(x)+cos_function(x)


def exponential_function(x):
    return 2**x


def complex_function(x):
    return pomocnicze.sin_function(x) + 3**x