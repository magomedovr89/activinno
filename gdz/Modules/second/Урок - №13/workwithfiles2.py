n = int(input('Введите значение n - '))
iter = 0
TasksInFile = []
while iter != n:
    task = input('Введите дело:')
    iter += 1
    TasksInFile.append(task + ', ')
# print(f' Ваши дела - {TasksInFile}')
file = open('YoursTasks.txt', 'a+')
i = 0
for elem in TasksInFile:
    if i % 2 == 0:
        file.write(elem)
    i += 1

file.close()
