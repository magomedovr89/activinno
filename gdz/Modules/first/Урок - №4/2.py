month = int(input('Введите чило месяца: '))
if month == 12 or month < 3 :
  print ("Зима")
elif 2 < month < 6 :
   print ("Весна")
elif 5 < month < 9 :
  print ("Лето")
elif 8 < month < 12 :
   print ("Осень")
elif 13 > month :
   print ("Месяцев всего 12")
