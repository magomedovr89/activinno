from time import time as time_now
from time import sleep as wait


def decorator(func):
    print('Старт/Декоратор')

    def wrapper(*args):
        start = time_now()
        print('Запуск функции')
        print(func(*args))
        end = time_now()
        print('Конец функции')
        results = (end - start)
        print('Время выполнения =', results)

    return wrapper


@decorator
def squaring(number):
    wait(0.3)
    return number ** 2


print('Начало')
squaring(4)
print('Конец')
