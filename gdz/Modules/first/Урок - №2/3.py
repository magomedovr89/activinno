PC = int(input('Введите количество компьютеров  - '))
if PC == 1:
    print(f"{PC} компьютер")
elif 1 < PC < 5:
    print(f"{PC} компьютера")
elif PC % 10 == 1:
    print(f'{PC} компьютер')
elif PC > 4:
    print(f"{PC} компьютеров")
