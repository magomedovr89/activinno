a = float(input('Введите первое значение - '))
operation = input('Введите операцию(*, +, -, /, **) ')
b = float(input('Введите второе значение - '))


def division(a, b):
    try:  # Для деления на ноль
        return print(a / b)
    except:
        print('Давайте без приколов пожалуйста')


def summa(a, b):
    return print(a + b)


def umnozhenie(a, b):
    return print(a * b)


def vichitanie(a, b):
    return print(a - b)


def exponentiation(a, b):
    return print(a ** b)
try:
    if operation == "+":
        summa(a, b)
    elif operation == "-":
        vichitanie(a, b)
    elif operation == "*":
        umnozhenie(a, b)
    elif operation == "**":
        exponentiation(a, b)
    elif operation == "/":
        division(a, b)
    else:
        print('Тут тоже без приколов пожалуйста')
except:
    print('Вы что-то не так сделали')



















