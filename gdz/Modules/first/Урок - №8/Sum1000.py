# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
range = range(1000 + 1)
summ = 0
for number in range:
    if number % 3 == 0 or number % 5 == 0:
        summ += number
print(summ)