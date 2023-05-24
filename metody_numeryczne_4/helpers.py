def horner(value, polynomial) -> float:
    result_horner = 0

    for i in polynomial:
        result_horner = result_horner * value + i

    return result_horner


def user_choose():

    user = int(input("Wybierz opcje: "))
    if user in [1, 2, 3, 4, 5, 6]:
        return user
    else:
        print("Bledny argument!!! Blad!!!!")
        exit(1)