def unikalno(lst):
    iter = 0
    i = 0
    for number in lst:
        povtors = lst.count(number)
        if povtors > 1:
            pass
            i = number
        else:
            iter += 1
    if iter > 0:
        print(f'Есть повторы в кол-ве {povtors}! Числа - {i}')
    else:
        print('Повторов нету!')


a = [1, 2, 3, 3, 4, 5]
unikalno(a)
print('____________________________')
print(f'Руслан, с новым годом!\U0001F973')
print(f'Счастья и здоровья вам!\U0001F973')
print(f'Чуть не забыл!Горячего чая!\U0001F973')
