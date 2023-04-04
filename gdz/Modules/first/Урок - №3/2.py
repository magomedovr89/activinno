lst = [1, 5, 8, 10, 138, 141, 237, 400]
for number in lst:
    if number % 2 == 0:
        print(number, end=' ')
    elif number == 237:
        break
