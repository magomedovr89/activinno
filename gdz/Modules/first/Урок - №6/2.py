number = input("Введите число - ")
reversNumber = number[-1]
for letter in number:
    if number == reversNumber:
        print("Число (number) палиндром")
    else:
        print("Число (number) не палиндром")

