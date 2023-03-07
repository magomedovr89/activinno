import itertools
from random import randint


n, k = input().split()
n = [randint(1, 10 ** 6) for i in range(int(n))]
k = int(k)





print(max((map(sorted, itertools.permutations(n, k))), key=lambda x: x[k // 2]))