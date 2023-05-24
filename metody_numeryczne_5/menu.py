import cheb_poly
import helpers
from cheb_poly import *
from sympy import *
import graf


def start():
    log = True
    x = Symbol('x')
    while (log):
        print("Wybierz funkcje: ")
        print('1) f(x) = x + 4 ')
        print('2) f(x) = 5x**3  + 3x +1')
        print('3) f(x) = |x|')
        print('4) f(x) = 2cos(x) + sin(x)')
        print('5) f(x) = |x|+cos(x)+4*x**2')
        print('6) Liniowa: x - 5')
        print('7) Wyjście')
        user = input('Wybierz operacje: ')

        if user == '1':
            func = x + 4
            function_dialog(func)
            log = False

        elif user == '2':
            #list = [5, 0, 3, 1]
            list = [17, 3, 8, -3]
            func = helpers.horner(x, list)
            function_dialog(func)
            log = False

        elif user == '3':
            func = abs(x)
            function_dialog(func)
            log = False

        elif user == '4':
            func = 2*cos(x)+sin(x)
            function_dialog(func)
            log = False
        elif user == '5':
            func = abs(x) + cos(x) + 4*x**2
            function_dialog(func)
            log = False
        elif user == '6':
            func = x - 5
            function_dialog(func)
            log = False
        elif user == '7':
            print('Zakonczenie programu. Do widzenia')
            exit(0)
        else:
            print('Niestety oskryptowalismy przypadek takiego bledu wiec teraz cie wyrzuci z programu')
            exit(1)

def function_dialog(func):
    print("Podaj przedział aproksymacji [x1,x2]")
    print('x1: ')
    x_1 = input()
    print("do: ")
    x_2 = input()
    print("Podaj stopień wielomianu aproksymującego: ")
    degree = input()
    print("Podaj liczbę węzłów: ")
    nodes = input()
    result = cheb_poly.Approximation(func, int(degree) + 1, int(nodes))
    print("Wielomian aproksymujący: ")
    print(result)
    error = cheb_poly.error_approx(float(x_1), float(x_2), func, int(degree), int(nodes))
    print("Błąd wynosi: ")
    print(error)
    graf.graf_print(float(x_1), float(x_2), func, int(degree), int(nodes))


