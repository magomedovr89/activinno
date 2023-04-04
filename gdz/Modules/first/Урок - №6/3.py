number = input("Введите число - ")
reversNumber = number[::-1]
if number == reversNumber:
        print("Это число палиндром")
else:
        print("Это число не палиндром")