import pomocnicze


def bisection_iterration(a, b, number_of_itarrations, func, *poly):

    if func(a, *poly) * func(b, *poly) >= 0:
        print('Bisekcja:\n')
        print("W podanym przedziale w danej funkcji nie znajduje sie miejsce zerowe")
        return -1
    i = 0
    m = a
    while i < number_of_itarrations:

        m = (a + b) / 2

        if func(m, *poly) * func(a, *poly) < 0:
            b = m
        elif func(m, *poly) * func(b, *poly) < 0:
            a = m

        i = i + 1

    print('\nMetoda bisekcji:')
    print("Wynik to : ", "%.6f" % m)
    print("Liczba iteracji: ", i)
    return m


def bisection_accuracy(a, b, epsilon, func, *poly):

    if func(a, *poly) * func(b, *poly) >= 0:
        print('Bisekcja:\n')
        print("W podanym przedziale w danej funkcji nie znajduje sie miejsce zerowe")
        return -1
    i = 0
    m = a
    while True:

        m = (a + b) / 2

        if func(m, *poly) * func(a, *poly) < 0:
            b = m
        elif func(m, *poly) * func(b, *poly) < 0:
            a = m

        if abs(func(m, *poly)) < epsilon:
            print('\nMetoda bisekcji:')
            print("Wynik to : ", "%.6f" % m)
            print("Liczhba iteracji: ", i)
            return m
        i += 1
