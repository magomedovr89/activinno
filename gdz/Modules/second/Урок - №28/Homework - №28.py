# Реализовать программу, которая рассчитывает площадь и периметр прямоугольника и обработать все возможное ошибки с помощью try..except.
def decorator(func):
    try:
        def value(a, b):
            try:
               x = func(a, b)
            except:
                print('Перепроверьте!\nЧто-то введено неверно!')
            return x
        return value
    except:
        print('Что-то не так')

@decorator
def square_and_perimeter_of_rectangle(a, b):
    a = float(a)
    b = float(b)
    if a < 1 or b < 1:
        print("Некретные значения!")
    else:
        return {'Площадь':(a*b),
                "Периметр":((a+b)*2)}




rectangle = square_and_perimeter_of_rectangle(input('Введите переменную a - '),input('Введите переменную b - '))
try:
    print('-'*10000)
    print(f'Площадь = {rectangle["Площадь"]} см**2,\n'
        f'Периметр = {rectangle["Периметр"]} см')
except:
    print('Код завершен!\nЧто-то пошло не по плану')
