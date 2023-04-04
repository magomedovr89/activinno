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
