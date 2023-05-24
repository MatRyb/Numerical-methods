#menu
import helpers as help
import functions as f
def main_menu():
    print('------------------------------------')
    print('Wybierz jedna z ponizszych funkcji: ')
    print('1) f(x) = x+4')
    print('2) f(x) = 3x^2 - 6x + 12')
    print('3) f(x) = 5^x3+3x +1')
    print('4) f(x) = sin(x) ')
    print('5) f(x) = 2cos(x) + sin(x)')
    print('6) f(x) = 2^x')
    print('-------------------------------------')

    user = help.user_choose()
    print('-----------------------')
    print('Wybeirz jedna z metod: ')
    print('1)Newtona-Cotes(eps)')
    print('2)Gauss wielomiany Czebyszewa(iter) ')
    print('-----------------------')

    user_method = int(input('podaj wybrana metode: '))

    if user_method == 1:
        eps = float(input('Podaj dokladnosc: '))
        print('Wynik: ')
        print('Wartosc dla Newtona-Cotesa: ' + str(f.border(user, eps)))

    elif user_method == 2:
        i = 2
        while i != 6:
            print('Liczba wezlow czebyszewa:  '+ str(i))
            print('Wartosc dla Gaussa-Czebyszewa: ' + str(f.Gauss(user,i)))
            i = i + 1