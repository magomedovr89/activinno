
Number = int(input('Введите нужное числовое значение - '))


def isPrime(Number):
    DivisorsList = []
    for number in range(1, Number):
        if Number % number == 0:
            DivisorsList.append(number)
    if len(DivisorsList) == 1:
        return print('Prime')
    else:
        return print('Not prime')


isPrime(Number)
