def caretaker_simulator(filename, i):
    i = int(i)
    if i == 3:
        with open(filename, 'r', encoding='utf-8') as f:
            x = f.readlines()
            print('-' * 43)
            for i in x:
                print('|%-19s|%s|%s|' % (
                ' '.join(i.strip().split()[:-2]), i.strip().split()[-2].center(10), i.strip().split()[-1].center(10)))
            print('-' * 43)
    elif i == 2:
        with open(filename, 'r', encoding='utf-8') as f:
            x = f.readlines()
            for i in x:
                print(i.strip())
    elif i == 5:
        with open(filename, 'r', encoding='utf-8') as f:
            c = 0
            for i in f.readlines():
                if 'банка' in i:
                    c += float(i.strip().split()[-1])
            print(c)
    elif i == 6:
        with open(filename, 'r', encoding='utf-8') as f:
            c = 0
            for i in f.readlines():
                if 'кг' in i:
                    c += float(i.strip().split()[-1])
            print(c)
    elif i == 7:
        with open(filename, 'r', encoding='utf-8') as f:
            c = 0
            for i in f.readlines():
                if 'рулон' in i:
                    c += float(i.strip().split()[-1])
            print(c)
    elif i == 4:
        n = input('введите единицы измерения (рулон, кг, банка)')
        a = []
        with open(filename, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                if n in i:
                    a.append(' '.join(i.strip().split()[:-2]) + i.strip().split()[-1] + '\n')
        f = open('exit.txt', 'w')
        for i in a:
            f.write(i)
        f.close()
    elif i == 8:
        print(str(sum(1 for line in open(filename, 'r', encoding='utf-8')))+'количество строк')
    elif i == 9:
        x = int(input('Введите ваш рост'))
        y = int(input('Введите ваш вес'))
        print('Ваш рост + вес = ' + str(x + y))
        print('Ваш рост + вес = ' + str(x) + str(y) + ' Я ДЖАВА СКРПИПТ')

def PrintMenu():
    print('---------------------------------------------------')
    print('1 : Прочитать файл ')
    print('2 : Вывести файл 1:1на экран ')
    print('3 : Вывести весь файл на экран ввиде таблиц ')
    print('4 : Сохранить в новый файл требуемые данные(кг, л, рулон) ')
    print('5 : Найти количество банок. ')
    print('6 : Найти количество килограмм. ')
    print('7 : Найти количество рулонов. ')
    print('8 : Количество строк хочешь узнать  мой  пользователь ?? ')
    print('9 : Prikol ')
    print('End (E) : Выход из программы')
    print('Menu (M) : вывод меню')

ar_to_end = ["end",'e','E','End']
ar_to_menu = ['Menu','menu','m','M']
PrintMenu()
name = input('Введите название файла с которым хотите работать: ')

user_chose = "Ya Molodec"
while user_chose not in ar_to_end :
    user_chose = input('Выберете операцию (Menu (M): показать меню ) :')
    if user_chose == '1':
        with open(name, 'r', encoding='utf-8') as f:
            file=f.readline()
        print('---------------------------------------------------')
    if user_chose == '2':
        caretaker_simulator(name,user_chose)
        print('---------------------------------------------------')
    if user_chose== '3':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '4':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '5':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '6':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '7':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '8':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose == '9':
        caretaker_simulator(name, user_chose)
        print('---------------------------------------------------')
    if user_chose in ar_to_menu:
        PrintMenu()
print('Конец')
