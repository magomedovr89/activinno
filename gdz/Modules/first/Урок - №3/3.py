a = [1, 2, 3, 4, 5, 6]
for number in a:
    if number % 2 == 1:
        a.remove(number)
    elif number == 4:
        a.remove(number)
        a.append(number // 2)