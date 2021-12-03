def caretaker_simulator(filename, i):
    i = int(i)
    if i == 3:
        with open(filename, 'r', encoding='utf-8') as f:
            x = f.readlines()
            print('-' * 43)
            for i in x:
                print('|%-19s|%s|%s|' % (
                    ' '.join(i.strip().split()[:-2]), i.strip().split()[-2].center(10),
                    i.strip().split()[-1].center(10)))
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
        print(sum(1 for line in open(filename, 'r', encoding='utf-8')))
    elif i == 9:
        x = int(input('Введите ваш рост'))
        y = int(input('Введите ваш вес'))
        print('Ваш рост + вес = ' + str(x + y))
        print('Ваш рост + вес = ' + str(x) + str(y) + 'Я ДЖАВА СКРПИПТ')
