import time
HowAreYou = input('Руслан, как ваши дела? '
                  '(В ответе хорошо или плохо)  - ')
if HowAreYou.upper() == 'ХОРОШО':
    print(f'Отлично!!! Хорошого дня!!!'
          f'{chr(129395)}{chr(129395)}{chr(129395)}')
elif HowAreYou.upper() == 'ПЛОХО':
    print(f'Надо выпить чаю, станет лучше!!! '
          f'{chr(129301)}{chr(129301)}{chr(129301)}')
else:
    print(f'Хорошо или плохо.')

time.sleep(2)
print('______________________')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, institution):
        super().__init__(name, age)
        self.institution = institution

    def get_institution(self):
        return self.institution


class Teacher(Student, Person):
    def __init__(self, name, age, institution, qualification):
        super().__init__(name, age, institution)
        self.qualification = qualification

    def get_qualification(self):
        return self.qualification


class Director(Teacher, Student, Person):
    def __init__(self, name, age, institution, qualification, experience):
        super().__init__(name, age, institution, qualification)
        self.experience = experience

    def get_experience(self):
        return self.experience


Pr = Person('Светлана', 95)
print('Человек:')
print(f'Имя - {Pr.name}')
print(f'Возраст - {Pr.age}')
print('______________________')

St = Student('Светлана', 95, 'Школа')
print('Ученик:')
print(f'Имя - {St.name}')
print(f'Возраст - {St.age}')
print(f'Учреждение - {St.institution}')
print('______________________')

Tr = Teacher('Светлана', 95, 'Школа', 'ПЕД')
print('Учитель:')
print(f'Имя - {Tr.name}')
print(f'Возраст - {Tr.age}')
print(f'Учреждение - {Tr.institution}')
print(f'Образование - {Tr.qualification}')
print('______________________')

Dr = Director('Светлана', 95, 'Школа', 'ПЕД', 50)
print('Директор:')
print(f'Имя - {Dr.name}')
print(f'Возраст - {Dr.age}')
print(f'Учреждение - {Dr.institution}')
print(f'Образование - {Dr.qualification}')
print(f'Опыт работы - {Dr.experience}')
print('______________________')

HowAreYou = input('Руслан, как ваши дела? '
                  '(В ответе хорошо или плохо)  - ')
if HowAreYou.upper() == 'ХОРОШО':
    print(f'Отлично!!! Хорошого дня!!!'
          f'{chr(129395)}{chr(129395)}{chr(129395)}')
elif HowAreYou.upper() == 'ПЛОХО':
    print(f'Надо выпить чаю, станет лучше!!! '
          f'{chr(129301)}{chr(129301)}{chr(129301)}')
else:
    print(f'Хорошо или плохо.')
