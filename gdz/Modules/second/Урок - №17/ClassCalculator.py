import time

HowAreYou = input('Руслан, как настроение? ')
time.sleep(2)
print(f'Можно лучше!!!\n\U0001F60E\U0001F60E\U0001F60E')
time.sleep(2)
class Calculator:
    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        return self.number * other.number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __truediv__(self, other):
        return self.number / other.number

a = Calculator(50)
b = Calculator(10)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
time.sleep(0.6)
print(f'Чаю все равно выпить можно!!!\n\U0001F60F\U0001F60F\U0001F60F')
