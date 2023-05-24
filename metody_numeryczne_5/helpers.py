import numpy as np

import helpers

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
    return cos_function(x)
    #return 2 * sin_function(x) + cos_function(x)


def function_abs(x):
    return np.abs(x);


def line_function(x):
    return 3 * x + 1

def complex_function(x):
    return helpers.sin_function(x) + function_abs(x) - 3
