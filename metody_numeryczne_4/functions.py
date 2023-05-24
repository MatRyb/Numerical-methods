import numpy as np
import math
import helpers
from numpy import double

def Gauss(function, countNode) -> double:
    result = 0
    i = 1
    while i <= countNode:
        actualWage = math.pi / countNode
        actualNode = -np.cos(((2*i-1) * math.pi)/(2*countNode))
        result += actualWage * FX(function, actualNode)
        i = i + 1
    return result
# obliczamy granice w celu wyliczenia calki Newtona-Cotesa
def border(function, eps) -> double:
    result = 0

    # granica do +1
    start = 0   #start

    end = 0.5   #koniec
    log = True  #log
    while log:
        temp = simpson(function, start, end, eps)
        result += temp
        start = end

        end = end + (0.5*(1-end))

        if math.fabs(temp) > eps:
            log = True
        else:
            log = False

    # granica do -1
    start = -0.5
    end = 0
    log = True
    while log:
        temp = simpson(function, start, end, eps)
        result += temp
        end = start
        start = start - ((1-math.fabs(end))*0.5)
        if math.fabs(temp) > eps:
            log = True
        else:
            log = False

    return result


# Simpsona - calka wg wzoru tego simpsona calego jakeigos
def simpson(funkcja, start, end, eps) -> float:
    bord1 = 1
    delta = end - start
    result = 0
    log = True
    while log:
        bord1 = bord1 * 2
        length = delta / bord1
        temp = result
        result = 0
        result += FXWX(funkcja, start) + FXWX(funkcja, end)
        for i in range(int(bord1 / 2)):
            result += 4 * FXWX(funkcja, start + (2 * i - 1) * length)
            result += 2 * FXWX(funkcja, start + (2 * i) * length)
            i += 1
        result *= length / 3
        if math.fabs(temp - result) > eps:
            log = True
        else:
            log = False
    return result

def FX(function, x) -> double:
    if function== 1:
        return x+4
    elif function == 2:
        return 3.0 * x * x -6.0 * x + 12
    elif function == 3:
        list = [5, 0, 3, 1]
        return helpers.horner(x, list)
    elif function == 4:
        return np.sin(x)
    elif function == 5:
        return np.cos(x)*2.0 + np.sin(x)
    elif function == 6:
        return 2**x
def FXWX(funkcja, x) -> double:
    return FX(funkcja, x) * (1 / np.sqrt(1 - x * x))
