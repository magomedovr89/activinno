number = int(input('Введите нужно число - '))
i = 0
res = 1
while i != number:
    i += 1
    res *= i
print(f'!{number} = {res}')


# number = int(input('Введите число - '))
# dividers = []
# for divider in range(2, number):
#     if number % divider == 0:
#         dividers.append(divider)
# if len(dividers) == 0:
#     print('prime')
# else:
#     print('not prime')