def value(h,v_1, v_2, m, g):
    return {'h': h, 'v_1': v_1, 'v_2': v_2, 'm': m, 'g': g}


def plane(h=100, v_1=20, v_2=0.5):
    return abs(round(((v_2 ** 2) - (v_1 ** 2)) / (2 * h), 2))


def time(v_1=20, v_2=0.5, acceleration=plane()):
    t = abs(round(((v_2 - v_1) / acceleration), 2))
    return t


def engine(m=20_000, g=1.63, acceleration=plane()):
    f = m * (g + acceleration)
    return f


# def Exisize moon-bot(answer):
#     if answer.upper() == 'ПРИМЕР':
#         title_of_plane = Label(frame, text=f'Ответ для стандартных значений:\n{plane()} м/с^2 - Ускорение при посадке.',font=25,bg='white').pack()
#         title_of_time = Label(frame, text=f'{time()} с - Время на изменение скорости.',font=25,bg='white').pack()
#         title_of_engine = Label(frame, text=f'{engine()} Н - Тяга двигателеей космического корабля.',font=25,bg='white').pack()
#     elif answer.upper() == 'ЗНАЧЕНИЯ':
#         try:
#             res = value()
#             title_of_plane= Label(frame,text=f'Ответ для значений:\n{plane(res["h"], res["v_1"], res["v_2"])} м/с^2 - Ускорение при посадке.',font=25,bg='white').pack()
#             title_of_time = Label(frame,text=f'{time(res["v_1"], res["v_2"], acceleration=plane())} с - Время на изменение скорости.',font=25,bg='white').pack()
#             title_of_engine = Label(frame,text=f'{engine(res["m"], res["g"], acceleration=plane())} Н - Тяга двигателеей космического корабля.',font=25,bg='white').pack()
#         except:
#             print('_' * 1000)
#             print('Вы ввели пустое значение(пробел) или поставили запятую вместо точки в десятичной дроби.\nПопробуйте еще раз, только правильно!')
#     elif answer.upper() == 'ВЫХОД':
#         Label(frame,text='Спасибо, что пришли!').pack()
#         exit()
#     else:
#         print('_' * 1000)
#         print(answer)
#         print('Вы ввели некорректное значение, перечитайте инструкцию!')
#
#
# def temp():
#     title.destroy()
#     Label(frame,text='Если хотите воспользоваться примером, нажмите - "Пример".\n'
#                      'Если хотите ввести соб. значения, нажмите - "Значения".\n'
#                      'Если не хотите мною воспользоваться, нажмите "Выход".\n'
#                      'Ваш выбор:',bg='white',font=35).pack()#fill=X)
#     Button(frame, text="Пример", command=btn1,font=5).pack()#fill=X)
#     Button(frame, text="Значения", command=btn2,font=5).pack()#fill=X)anchor="center",fill=X)
#     Button(frame, text="Выход", command=btn3,font=5).pack()#fill=X)
#     FirstButton.destroy()
#
#
# def btn1():
#     answer = 'Пример'
#     return Exisize moon-bot(answer)
#
#
# def btn2():
#     answer = 'Значения'
#     return Exisize moon-bot(answer)
#
#
# def btn3():
#     answer = 'Выход'
#     return Exisize moon-bot(answer)



