#Сделано все на отлично, но хочется шикарно так что попробуй использовать классы и спец методы для математический операций.
from modules import *
import re
while True:
    while True:
        try:
            try:
                a = Calculator(round(float(input('Введите первое значение - ')), 3))
                break
            except ValueError:
                print('Введено неверное значение')
        except:
            print('Что-то пошло не так')
    while True:
        try:
            operation = input('Введите операцию(*, +, -, /) ')
            if re.match('[*, +, -, /]', operation):
                break
            else:
                print('Операция введена неверно')
        except:
            print('Перепроверьте операцию')
    while True:
        try:
            try:
                b = Calculator(round(float(input('Введите второе значение - ')), 3))
                break
            except ValueError:
                print('Введено неверное значение!')
        except:
            print('Что-то пошло не так!')
    try:
        if operation == "+":
            try:
                print(f' Итого - {round((a - b), 3)}')
            except:
                print('Сложение не произведенно')
        elif operation == "-":
            try:
                print(f'Итого - {round((a - b), 3)}')
            except:
                print('Вычитание не произведенно')
        elif operation == "*":
            try:
                print(f'Итого - {round((a * b), 3)}')
            except:
                print('Умножение не произведенно')

        elif operation == "/":
            try:
                try:
                    print(f'Итого - {round((a / b), 3)}')
                except ZeroDivisionError:
                    print('На ноль делить нельзя')
            except:
                print('Деление не произведенно')
        else:
            print('Что-то пошло не так')
    except:
        print('Вы что-то не так сделали')
