def sieczne_iteration(x1, x2, number_of_iterations, func, *func_arg):

    if func(x1, *func_arg) * func(x2, *func_arg) >= 0:
        print('Sieczna:\n')
        print("W podanym przedziale w danej funkcji nie znajduje sie miejsce zerowe")
        return -1

    i = 0

    while i < number_of_iterations:
        fx1 = func(x1, *func_arg)
        fx2 = func(x2, *func_arg)

        x3 = x1 - (x1 - x2) * fx1 / (fx1 - fx2)

        if x2 != x3:
            x1 = x2
            x2 = x3

        i += 1

    print('\nMetoda siecznych:')
    print("Wynik to : ", "%.6f" % x3)
    print("Liczba iteracji: ", i)
    return x3


def sieczne_epsilon(x1, x2, epsilon, func, *func_arg):

    if func(x1, *func_arg) * func(x2, *func_arg) >= 0:
        print('Sieczna:\n')
        print("W podanym przedziale w danej funkcji nie znajduje sie miejsce zerowe")
        return -1

    i = 0

    while True:
        fx1 = func(x1, *func_arg)
        fx2 = func(x2, *func_arg)

        x3 = x1 - (x1 - x2) * fx1 / (fx1 - fx2)

        if x2 != x3:
            x1 = x2
            x2 = x3

        if abs(func(x3, *func_arg)) < epsilon:
            print('\nMetoda siecznych:')
            print("Wynik to : ", "%.6f" % x3)
            print("Liczba iteracji: ", i)
            return x3

        i += 1
