if __name__ == "__main__":
    from tkinter import *
    from Telegram_Bot import functions
    from tkinter import messagebox

    root = Tk()

    def SecondFrame_destroy():#Отчистака второго фрейма
        global SecondFrame
        SecondFrame.destroy()
        SecondFrame = Frame(root, bg='white')
        SecondFrame.place(relwidth=1, y=300, x=0, relheight=1)

    def value():  # Тут надо получить значение из функции (h, v_1, v_2, g, m) из 'Entry'
        # Тут основная проблема проблема, не получается правильно реализовать функцию
        global SecondFrame, hight, g, h, v_1, v_2, m

        def get_h():# Тут надо получить значение h
            global SecondFrame, first_speed_entr, hight
            h = hight.get()
            h = float(h)

            SecondFrame_destroy()
            # Строка, текст, кнопака для получения значение v_1
            first_speed_str = Label(SecondFrame, text='Начальная скорость:', font=25, bg='white')
            first_speed_str.pack()

            first_speed_entr = Entry(SecondFrame)
            first_speed_entr.pack()

            first_speed_button = Button(SecondFrame, text='Далее', command=get_v_1)
            first_speed_button.pack()
            print(h)

            return h

        def get_v_1():# Тут надо получить значение v_1
            global SecondFrame, first_speed_entr, first_speed_strr, first_speed_button, second_speed_entr
            v_1 = first_speed_entr.get()
            v_1 = float(v_1)

            SecondFrame_destroy()
            # Строка, текст, кнопака для получения значение v_2
            second_speed_str = Label(SecondFrame, text='Конечная скорость:', font=25, bg='white')
            second_speed_str.pack()

            second_speed_entr = Entry(SecondFrame)
            second_speed_entr.pack()

            second_speed_button = Button(SecondFrame, text='Далее', command=get_v_2)
            second_speed_button.pack()
            print(v_1)
            return v_1

        def get_v_2():# Тут надо получить значение v_2
            global SecondFrame, second_speed_str, second_speed_entr, second_speed_button, massa_entr
            v_2 = second_speed_entr.get()
            v_2 = float(v_2)

            SecondFrame_destroy()
            # Строка, текст, кнопака для получения значение m
            massa_str = Label(SecondFrame, text='Масса коробля:', font=25, bg='white')
            massa_str.pack()

            massa_entr = Entry(SecondFrame)
            massa_entr.pack()

            massa_button = Button(SecondFrame, text='Далее', command=get_m)
            massa_button.pack()
            print(v_2)
            return v_2

        def get_m():# Тут надо получить значение m
            global SecondFrame, massa_str, massa_entr, massa_button, massa_entr
            m = massa_entr.get()
            m = float(m)
            print(m)
            SecondFrame_destroy()

            Button(SecondFrame, text='Далее', command=get_g).pack()
            return m

        def get_g():#Тут надо получить значение g
            global SecondFrame, v_1, h, g, v_2, m
            g = 0

            def mars():# Функции для получения значения g
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 3.7
                return g

            def luna():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 1.63
                return g

            def mercury():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 3.7
                return g

            def earth():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 9.8
                return g

            def venus():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 8.87
                return g

            def jupiter():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 24.8
                return g

            def saturn():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 10.4
                return g

            def uranus():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 8.87
                return g

            def neptune():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 10.15
                return g

            def pluto():
                global SecondFrame, g
                SecondFrame_destroy()
                Button(SecondFrame, text='Результат', command=results).pack()
                g += 0.66
                return g

            def sun():
                global SecondFrame, g
                SecondFrame_destroy()
                g += 274
                Button(SecondFrame, text='Результат', command=results).pack()
                return g

            SecondFrame_destroy()

            Button(SecondFrame, text='Меркурий', command=mercury).pack()
            Button(SecondFrame, text='Венера', command=venus).pack()
            Button(SecondFrame, text='Земля', command=earth).pack()
            Button(SecondFrame, text='Марс', command=mars).pack()
            Button(SecondFrame, text='Юпитер', command=jupiter).pack()
            Button(SecondFrame, text='Сатурн', command=saturn).pack()
            Button(SecondFrame, text='Уран', command=uranus).pack()
            Button(SecondFrame, text='Нептун', command=neptune).pack()
            Button(SecondFrame, text='Плутон', command=pluto).pack()
            Button(SecondFrame, text='Луна', command=luna).pack()
            Button(SecondFrame, text='Солнце', command=sun).pack()
            print(g)
            return g


        def results():
            global h, v_1, v_2, m, g
            SecondFrame_destroy()
            return {'h': h, 'v_1': v_1, 'v_2': v_2, 'm': m, 'g': g}


        Label(SecondFrame, text='Введите высоту:', font=25, bg='white').pack()
        hight = Entry(SecondFrame)#Создание строки
        hight.pack()
        Button(SecondFrame, text='Далее', command=get_h).pack()#Запуск функции get_h()
        return {'h': 100, 'v_1': 20, 'v_2': 0.5, 'm': 20000, 'g': 1.63} # Функция пробегает без ограничений, как это исправить? Возврат для функции values()

        # return {'h': h, 'v_1': v_1, 'v_2': v_2, 'm': m, 'g': g}# Нужно вернуть этот словарь со значениями

    def moon(answer):# Функция проверки и вывода результата
        global SecondFrame
        if answer.upper() == 'ПРИМЕР':
            SecondFrame_destroy()
            Label(SecondFrame, text=f'Ответ для стандартных значений:\n'
                                    f'{functions.plane()} м/с^2 - Ускорение при посадке.', font=25, bg='white').pack()
            Label(SecondFrame, text=f'{functions.time()} с - '
                                    f'Время на изменение скорости.', font=25, bg='white').pack()
            Label(SecondFrame, text=f'{functions.engine()} Н'
                                    f' - Тяга двигателеей космического корабля.', font=25, bg='white').pack()
        elif answer.upper() == 'ЗНАЧЕНИЯ':
            try:
                SecondFrame_destroy()
                res = value()
                str1 = f'Ответ для значений:\n{functions.plane(res["h"], res["v_1"], res["v_2"])} м/с^2 - Ускорение при посадке.'
                str2 = f'{functions.time(res["v_1"], res["v_2"], acceleration=functions.plane())} с - Время на изменение скорости.'
                str3 = f'{functions.engine(res["m"], res["g"], acceleration=functions.plane())} Н - Тяга двигателеей космического корабля.'
                messagebox.showinfo(title='Ответ', message=f'{str1}\n{str2}\n{str3}')
                Label(SecondFrame, text='высота', font=25, bg='white').pack()
                Label(SecondFrame, text='длинна', font=25, bg='white').pack()
                Label(SecondFrame, text='ширина', font=25, bg='white').pack()
            except AttributeError:
                print('Не работает тут')
                # messagebox.showerror(title='Ошибка!', message='Вы ввели пустое значение(пробел) или поставили запятую вместо точки в десятичной дроби.\nПопробуйте еще раз, только правильно!').pack()

        elif answer.upper() == 'ВЫХОД':
            Label(frame, text='Спасибо, что пришли!').pack()
            exit()

        else:
            print('_' * 1000)
            print(answer)
            messagebox.showerror(title='Ошибка!',message='Вы ввели пустое значение(пробел) или поставили запятую вместо точки в десятичной дроби.\nПопробуйте еще раз, только правильно!')
            print('Вы ввели некорректное значение, перечитайте инструкцию!')

    def btn1():
        answer = 'ПРИМЕР'
        return moon(answer)

    def btn2():
        answer = 'ЗНАЧЕНИЯ'
        return moon(answer)

    def btn3():
        answer = 'ВЫХОД'
        return moon(answer)

    def temp():# Временная функция
        title.destroy()
        Label(frame, text='Если хотите воспользоваться примером, нажмите - "Пример".\n'
                         'Если хотите ввести соб. значения, нажмите - "Значения".\n'
                          'Если хотите увидеть задачу - "Задача"\n '
                          'Если не хотите мною воспользоваться, нажмите "Выход"\n'
                         'Ваш выбор:', bg='white', font=35).pack(fill=X)
        Button(frame, text="Пример", command=btn1, font=5).pack(fill=X)
        Button(frame, text="Значения", command=btn2, font=5).pack(fill=X)
        Button(frame, text="Задача", command=start, font=5).pack(fill=X)
        Button(frame, text="Выход", command=btn3, font=5).pack(fill=X)
        FirstButton.destroy()

    root['bg'] = '#fafafa'  # Цвет окна
    root.title('Расчет космических тел')  # Название окна

    root.geometry('600x600')  # Размер окна

    root.resizable(width=True, height=True)  # Разрешение на именения окна

    canvas = Canvas(root, height=600, width=600, bg='white') # Создание канваса
    canvas.pack()

    frame = Frame(root, bg='white')  # Первый фрейм

    SecondFrame = Frame(root, bg='green')  # Второй фрейм

    def start():  # Функция для запуска начального экрана
        global FirstButton, title, frame, SecondFrame
        frame.destroy()
        SecondFrame.destroy()
        frame = Frame(root, bg='white')
        frame.place(relwidth=1, relheight=0.6)
        title = Label(frame, text='Привет! Я -  программа, помогающая учёным рассчитывать значения,\n'
                                  ' необходимые для посадки космического корабля на любую планету.\n'
                                  'Для примера я могу показать значения для посадки корабля,\n '
                                  'массой 20тыс. кг., на луну, при начальной скорости - 20м/с и конечной - 0.5м/с,\n'
                                  'находящегося на высоте 100м.', bg='white', font=35)#, foreground='white'
        title.pack(fill=X)
        FirstButton = Button(frame, text="Понятно", command=temp, font=5)
        FirstButton.pack(fill=X)

    start()# Запуск начального экрана

    root.mainloop()  # Бесконечный цикл для работы программы



