try:
    n = int(input("Введите количество дел -  "))
    list = []
    for i in range(n):
        a = str(input("Введите дело -  "))
        list.append(a)
    f = open("spisok del.txt", "w+")
    for element in list:
        if element % 2 == 0:
            f.write(element + '')
        element += 1
    f.close()

except:
    print(f'Ошибка')