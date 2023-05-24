import numpy as np
import matplotlib.pyplot as plt

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



def function_abs(x):
    return np.abs(x);


def line_function(x):
    return 3 * x + 1


def complex_function(x):
    return helpers.sin_function(x) + function_abs(x) - 3


def user_choose(x, tab, user):
    if user == '1':
        return line_function(x)
    elif user == '2':
        return function_abs(x)
    elif user == '3':
        return horner(x, tab)
    elif user == '4':
        return trygonemetric_function(x)
    elif user == '5':
        return complex_function(x)


def interpolation(a, b, file_arguments, calculated_file, len, arguments2, values2):

    for i in np.arange(a, b, 0.01):

        y = 0.0

        for j in range(0, len):
            help_val = np.double(calculated_file[j])
            for k in range(0, len):
                if j != k:
                    help_val *= ((i - file_arguments[k]) / (file_arguments[j] - file_arguments[k]))
            y = y + help_val
        arguments2.append(i)
        values2.append(y)


def knots(a, b, flag, arguments, calculated_values, tab):
    for i in np.arange(a, b, 0.01):
        arguments.append(i)
        calculated_values.append(user_choose(i, tab, flag))
