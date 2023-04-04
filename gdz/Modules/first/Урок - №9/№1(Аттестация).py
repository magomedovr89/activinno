a = int(input('a = '))
b = int(input('b = '))
sum = 0
j = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        j += 1

print(sum / j)
