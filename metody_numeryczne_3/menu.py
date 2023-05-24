import numpy as np
import helpers
import wykresy


def menu_for_users():
    a, b = 0.0, 0.0

    function_parameters = [-2, 3, 2, -4, 0] #do hornera
    #function_parameters = [ 1, -4, 0, 14]  # do hornera
    #function_parameters = [ 8,-2, 4]  # do hornera
    arguments = []
    values = []
    print("Program interpoluje dana funkcje metoda Lagrange'a dla nierownych odstepow argumentu. \n")
    print("Dane dotyczace wezlow pobierane sa z pliku pom.txt. Użytkownik jest proszony go wypełnić przed wygenerowaniem wykresów\n")
    print("Wybierz funkcje: \n "
                   "1. Funkcja liniowa y = 3x+1 \n "
                   "2. Funkcja modul:   y = |x| \n "
                   "3. Wielomian: y = -x^3+5x+3\n "
                   "4. Funkcja trygonometryczna 2*sin(x)+cos(x) \n "
                   "5. Zlozenie funkcji\n"
          " 6. Wyjscie")

    user = input('Wybierz opcje: ')

    if user == '1' or user == '2' or user == '3' or user == '4' or user == '5':
        print("Okresl przedzial")
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
    elif user == '6':
        exit(0);
    else:
        print("Blad!! Wybrałeś nieprawidłową opcję, dlaczego :---( ?")
        exit(1)

    helpers.knots(a, b, user, arguments, values, function_parameters)
    file_par = np.loadtxt("pom.txt", dtype='d')
    calculated_file = helpers.user_choose(file_par, function_parameters, user)


    arguments2 = []
    values2 = []
    helpers.interpolation(a, b, file_par, calculated_file, len(file_par), arguments2, values2)
    wykresy.wykres(a, b, arguments, values, file_par, arguments2, values2, calculated_file)

    index = 0



    for i in arguments2:
        if arguments2 == 0.0:
            index = i
    print(values2[index])
