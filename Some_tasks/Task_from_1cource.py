from math import *

subject = {
    'Информатика':
        {7, 14, 20, 27, 34, 40, 42, 44, 46, 48, 50, 51, 53, 55, 57, 59, 61, 62, 64, 66, 68, 70, 72, 73,
         75, 77, 79, 81, 83, 84, 88, 91, 94, 97, 100},
    'Биология':
        {3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36, 38, 39, 40, 42, 43, 44, 46, 47, 48, 50, 51, 52,
         53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 79, 82, 84, 86, 89, 91, 93,
         96, 98, 100},
    'Физика':
        {4, 7, 10, 14, 17, 20, 23, 27, 30, 33, 36, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54,
         55, 57, 58, 59, 60, 61, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100},

    'Математика':
        {5, 9, 14, 18, 23, 27, 33, 39, 45, 50, 56, 62, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96,
         98, 99, 100},

    'География ':
        {4, 7, 11, 14, 17, 21, 24, 27, 31, 34, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53,
         54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 74, 78, 83, 87, 92, 96, 100},

    'Литература':
        {3, 5, 7, 9, 11, 13, 15, 18, 20, 22, 24, 26, 28, 30, 32, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 47, 48, 49,
         50, 51, 52, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 77, 80, 84, 87, 90, 94, 97,
         100},

    'Химия':
        {3, 6, 9, 12, 14, 17, 20, 23, 25, 28, 31, 34, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52,
         53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 83, 86,
         89, 92, 95, 98, 100},

    'История':
        {4, 8, 11, 15, 18, 22, 25, 29, 32, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52,
         54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 75, 77, 79, 82, 84, 86, 89, 91, 93, 96, 98,
         100},

    'Обществознание':
        {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 42, 44, 45, 46, 47, 48, 49, 51,
         52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 74, 76, 77, 79, 81, 82, 84, 86, 87,
         89, 91, 92, 94, 96, 97, 99, 100}
}
subject0 = {
    'Информатика':
        {3, 5, 7, 11, 13, 37, 41, 43, 47, 59, 61, 71, 73, 97},
    'Биология':
        {3, 5, 7, 23, 43, 47, 53, 59, 61, 73, 79, 89},
    'Физика':
        {7, 17, 23, 41, 47, 53, 59, 61},

    'Математика':
        {5, 23},

    'География ':
        {7, 11, 17, 31, 37, 41, 43, 47, 53, 61, 67, 83},

    'Литература':
        {3, 5, 7, 11, 13, 37, 41, 43, 47, 59, 61, 71, 73, 97},

    'Химия':
        {3, 17, 23, 31, 41, 43, 47, 53, 61, 67, 71, 73, 79, 83, 89},

    'История':
        {11, 29, 37, 41, 43, 47, 61, 67, 71, 79, 89},

    'Обществознание':
        {2, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 79, 89, 97}
}
""" Функция resheto реализует решето Эратосфена  """


def resheto(n):
    N = 2
    s = set(range(2, n + 1))
    for i in range(2, int(sqrt(n) + 1)):
        if i in s:
            s -= set(range(i * i, n + 1, i))
    k = set(range(2, 2))
    s -= k
    return s


def prostoe(subj):
    return subj.intersection(resheto(100))


'''Функиця  razn заменяет & для множеств.
   Почему так?
   Ну вот так получилось '''


def razn(a, b):
    c = 0
    for i in a:
        if i in b:
            c += 1
    if c >= 2:
        return True
    else:
        return False


# Меню это меню
def menu():
    choseed = set()
    print('Введите 1 если хотите ввывести  этот предмет ')
    print("Введите 0 если не хотите вывести  этот предмет 0 ")
    for i in subject:
        print(i, end=': ')
        if input() == '1':
            choseed.add(i)
        print()
    return choseed


print('Режимы работы :')
print('1: если хотите  самостоятельно вводить название  предметов ')
print('2: если хотите только выбирать  по средству нажатия клавиши 1 ')
chose = input('Выберите режим работы : ')
if chose == '1':
    user_input = input('Ведите предметы  которые вы хотите вывести с  большой буквы ')
    user_input = user_input.split()
    # Проверка на   правильность    введенных данных
    user_input_prav = ['Информатика''Биология', 'Физика', 'Математика', 'География ', 'Литература', 'Химия', 'История',
                       'Обществознание']
    count = 0
    a = []
    i = 0
    while i < len(user_input):
        if user_input[i] not in user_input_prav:
            count += 1
            a.append(user_input[i])
            user_input.remove(user_input[i])
        i += 1
    if count == 1:
        print('Нет данных по  предметам ', end='  ')
        for i in a:
            print(i, end='  ')
    if count == 2:
        print('Нет данных по  предметам ', end='  ')
        for i in range(len(a)):
            if i < (len(a) - 1):
                print(a[i], end=', ')
            else:
                print(a[i], end=' ')
    # Выводим предметы которые выбрал ползовател
    print('\n')
    print('Выбранные предметы ', end=' ')

    for i in user_input:
        print(i, end=', ')
    print('\n')

    for i in user_input:
        print(i, ': ', end=' ')
        f = sorted(list(prostoe(subject[i])))
        for j in f:
            print(j, end=' ')
        print()
    # Принтим пары предметов если совпадает 2 их тестовых балла
    print('Задание  1 ')
    for i in range(len(user_input)):
        for j in range(i + 1, len(user_input)):
            if razn(subject0[user_input[i]], subject0[user_input[j]]) == True:  print(user_input[i], ' ', user_input[j])

    print('\n')
    print('Задание  2 ')
    # Выводим как оно должно выглядеть в латехе
    for i in user_input:
        n = str(i) + ' & '
        for j in sorted(list(prostoe(subject[i]))):
            n += str(j) + ' '
        n += '\\' + '\\' + '\n\hline'
        print(n)
    print('\\end{tabular}')

    m = open('Tabl.tex', 'w+')
    h = '\\begin{tabular}{|c|l|}\n\\hline\n\Предмет & Баллы \\' + '\\' + '\n\hline\n'

    m.write(h)

    for i in user_input:
        n = str(i) + ' & '
        for j in sorted(list(prostoe(subject[i]))):
            n += str(j) + ' '
        n += '\\' + '\\' + '\n\hline\n'
        m.write(n)
    m.write('\\end{tabular}')
    m.close()

    input('Press ENTER to exit')

if chose != '1' and chose != '2':
    print('Ошибка')

if chose == '2':
    user_input = list(menu())

    print('Выбранные предметы ', end=' ')
    for i in user_input:
        print(i, end=' ')

    print('\n')
    for i in user_input:
        print(i, ': ', end=' ')
        f = sorted(list(prostoe(subject[i])))
        for j in f:
            print(j, end=',')
        print()
    # Принтим пары предметов если совпадает 2 их тестовых балла
    print('Задание  1 ')
    for i in range(len(user_input)):
        for j in range(i + 1, len(user_input)):
            if razn(subject0[user_input[i]], subject0[user_input[j]]) == True:  print(user_input[i], ' ', user_input[j])
    # Выводим как оно должно выглядеть в латехе
    print('\n')
    print('Задание  2 ')
    print('\\begin{tabular}{|c|l|}\n\\hline\n\Предмет & Баллы \\' + '\\' + '\n\hline')
    for i in user_input:
        n = str(i) + ' & '
        for j in sorted(list(prostoe(subject[i]))):
            n += str(j) + ' '
        n += '\\' + '\\' + '\n\hline'
        print(n)
    print('\\end{tabular}')

    m = open('Tabl.tex', 'w+')
    h = '\\begin{tabular}{|c|l|}\n\\hline\n\Предмет & Баллы \\' + '\\' + '\n\hline\n'

    m.write(h)

    for i in user_input:
        n = str(i) + ' & '
        for j in sorted(list(prostoe(subject[i]))):
            n += str(j) + ' '
        n += '\\' + '\\' + '\n\hline\n'
        m.write(n)
    m.write('\\end{tabular}')
    m.close()
