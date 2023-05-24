import bisekcja
import pomocnicze
import sieczne
import matplotlib.pyplot as plt
import numpy as np


def choose_menu():

    log = 1
    wielomian_test = [-1, 0, 5, 3]
    while log:
        print('.......MENU.......')
        print('1) -x^3+5x+3')
        print('2) 2*sin(x)+cos(x)')
        print('3) 2^x')
        print('4) Funkcja zlozona')
        print('5) Wyjscie z programu ')
        print('...................')
        user = input('Wybierz opcje: ')

        if user == '1':

            ix = np.linspace(-10, 10, 100)
            iy = np.array([pomocnicze.horner(ix[i], wielomian_test) for i in range(len(ix))])

            fig1, ax1 = plt.subplots()
            ax1.plot(ix, iy)
            ax1.grid(True)
            ax1.axhline(y=0, color='k')
            ax1.axvline(x=0, color='k')
            plt.show()

            a = int(input('Podaj poczatek przedzialu: '))
            b = int(input('Podaj koniec przedzialu'))

            print('.....MENU......')
            print('1 - epsilon')
            print('2 - iteracja')

            choose_kryt = input('Podaj warunek stopu: ')

            if choose_kryt == '1':
                eps = float(input('Podaj dokladnosc: '))
                wielomian = [-1, 0, 5, 3]
                x1 = bisekcja.bisection_accuracy(a, b, eps, pomocnicze.horner, wielomian)
                x2 = sieczne.sieczne_epsilon(a, b, eps, pomocnicze.horner, wielomian)
                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.horner(x[i], wielomian) for i in range(len(x))])
                fig, ax = plt.subplots()
                ax.scatter(x1, pomocnicze.horner(x1,wielomian), s=50, c='red',marker="^")
                ax.scatter(x2, pomocnicze.horner(x2, wielomian), s=50, c='blue', marker="o")
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()
                log = 0

            elif choose_kryt == '2':
                iter = int(input('Podaj liczbe iteracji:'))
                wielomian = [-1, 0, 5, 3]
                x1 = bisekcja.bisection_iterration(a, b, iter, pomocnicze.horner, wielomian)
                x2 = sieczne.sieczne_iteration(a, b, iter, pomocnicze.horner, wielomian)
                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.horner(x[i], wielomian) for i in range(len(x))])
                fig, ax = plt.subplots()
                ax.scatter(x1, pomocnicze.horner(x1, wielomian), s=50, c='red', marker="^")
                ax.scatter(x2, pomocnicze.horner(x2, wielomian), s=50, c='blue', marker="o")
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()
                log = 0

        elif user == '2':

            ix = np.linspace(-50, 50, 1000)
            iy = np.array([pomocnicze.trygonemetric_function(ix[i]) for i in range(len(ix))])

            fig1, ax1 = plt.subplots()
            ax1.plot(ix, iy)
            ax1.grid(True)
            ax1.axhline(y=0, color='k')
            ax1.axvline(x=0, color='k')
            plt.show()



            a = int(input('Podaj poczatek przedzialu: '))
            b = int(input('Podaj koniec przedzialu'))

            print('.....MENU......')
            print('1 - epsilon')
            print('2 - iteracja')

            choose_kryt = input('Podaj warunek stopu: ')

            if choose_kryt == '1':
                eps = float(input('Podaj dokladnosc: '))
                x1 = bisekcja.bisection_accuracy(a, b, eps, pomocnicze.trygonemetric_function)
                x2 = sieczne.sieczne_epsilon(a, b, eps, pomocnicze.trygonemetric_function)

                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.trygonemetric_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.scatter(x1, pomocnicze.trygonemetric_function(x1), s=50, c='red', marker="^")
                ax.scatter(x2, pomocnicze.trygonemetric_function(x2), s=50, c='blue', marker="o")
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

                log = 0

            elif choose_kryt == '2':
                iter = int(input('Podaj liczbe iteracji:'))
                x1 = bisekcja.bisection_iterration(a, b, iter, pomocnicze.trygonemetric_function)
                x2 = sieczne.sieczne_iteration(a, b, iter, pomocnicze.trygonemetric_function)
                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.trygonemetric_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

            log = 0

        elif user == '3':

            ix = np.linspace(-10, 10, 100)
            iy = np.array([pomocnicze.exponential_function(ix[i]) for i in range(len(ix))])

            fig1, ax1 = plt.subplots()
            ax1.plot(ix, iy)
            ax1.grid(True)
            ax1.axhline(y=0, color='k')
            ax1.axvline(x=0, color='k')
            plt.show()

            a = int(input('Podaj poczatek przedzialu: '))
            b = int(input('Podaj koniec przedzialu'))

            print('.....MENU......')
            print('1 - epsilon')
            print('2 - iteracja')

            choose_kryt = input('Podaj warunek stopu: ')

            if choose_kryt == '1':
                eps = float(input('Podaj dokladnosc: '))
                x1 = bisekcja.bisection_accuracy(a, b, eps, pomocnicze.exponential_function)
                x2 = sieczne.sieczne_epsilon(a, b, eps, pomocnicze.exponential_function)

                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.exponential_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

                log = 0

            elif choose_kryt == '2':
                iter = int(input('Podaj liczbe iteracji:'))
                x1 = bisekcja.bisection_iterration(a, b, iter, pomocnicze.exponential_function)
                x2 = sieczne.sieczne_iteration(a, b, iter, pomocnicze.exponential_function)

                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.exponential_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

                log = 0

        elif user == '4':

            ix = np.linspace(-10, 10, 100)
            iy = np.array([pomocnicze.complex_function(ix[i]) for i in range(len(ix))])

            fig1, ax1 = plt.subplots()
            ax1.plot(ix, iy)
            ax1.grid(True)
            ax1.axhline(y=0, color='k')
            ax1.axvline(x=0, color='k')
            plt.show()

            a = int(input('Podaj poczatek przedzialu: '))
            b = int(input('Podaj koniec przedzialu'))

            print('.....MENU......')
            print('1 - epsilon')
            print('2 - iteracja')

            choose_kryt = input('Podaj warunek stopu: ')

            if choose_kryt == '1':
                eps = float(input('Podaj dokladnosc: '))
                x1 = bisekcja.bisection_accuracy(a, b, eps, pomocnicze.complex_function)
                x2 = sieczne.sieczne_epsilon(a, b, eps, pomocnicze.complex_function)

                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.complex_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.scatter(x1, pomocnicze.complex_function(x1), s=50, c='red', marker="^")
                ax.scatter(x2, pomocnicze.complex_function(x2), s=50, c='blue', marker="o")
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

                log = 0

            elif choose_kryt == '2':
                iter = int(input('Podaj liczbe iteracji:'))
                x1 = bisekcja.bisection_iterration(a, b, iter, pomocnicze.complex_function)
                x2 = sieczne.sieczne_iteration(a, b, iter, pomocnicze.complex_function)

                x = np.linspace(a, b, 1000)
                y = np.array([pomocnicze.complex_function(x[i]) for i in range(len(x))])

                fig, ax = plt.subplots()
                ax.scatter(x1, pomocnicze.complex_function(x1), s=50, c='red', marker="^")
                ax.scatter(x2, pomocnicze.complex_function(x2), s=50, c='blue', marker="o")
                ax.plot(x, y)
                ax.grid(True)
                ax.axhline(y=0, color='k')
                ax.axvline(x=0, color='k')
                plt.show()

                log = 0

        elif user == '5':
            log = 0

