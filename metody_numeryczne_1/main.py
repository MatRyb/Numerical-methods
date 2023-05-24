import menu


def horner(value, polynomial) -> float:
    result_horner = 0

    for i in polynomial:
         result_horner = result_horner * value + i

    return result_horner

if __name__ == '__main__':

    menu.choose_menu()

