'''Геном жителей системы Тау Кита содержит 26 видов оснований, для обозначения которых будем использовать буквы латинского алфавита от A до Z,
а сам геном записывается строкой из латинских букв. Важную роль в геноме играют пары соседних оснований, например,
 в геноме «ABBACAB» можно выделить следующие пары оснований: AB, BB, BA, AC, CA, AB.

Степенью близости одного генома другому геному называется количество пар соседних оснований первого генома, которые встречаются во втором геноме.
Вам даны два генома, определите степень близости первого генома второму геному. Программа получает на вход две строки, состоящие из заглавных латинских букв.
 Каждая строка непустая, и её длина не превосходит 105.
Программа должна вывести одно целое число – степень близости генома, записанного в первой строке, геному, записанному во второй строке.'''

def genom_set(gen : str):
    res = []
    for i in range(len(gen)-1):
        res.append(gen[i]+gen[i+1])
    # print(res)
    return set(res)
def genom_dict(gen : str ):
    res = dict()
    for i in range(len(gen)-1):
        try:
            res[gen[i]+gen[i+1]]+=1
        except KeyError :
            res[gen[i]+gen[i+1]] = 1
    return res


if __name__ == '__main__':
    genom1 = input().upper()
    gen_dict = genom_dict(genom1)
    # gen_set1 = genom_set(genom1)
    genom2 = input().upper()
    gen_set1 = genom_set(genom2)
    near_gen = 0
    for i in gen_set1:
        # print(i)
        try:
            x = gen_dict[i]

            near_gen += x
        except KeyError:
            pass
    print(near_gen)
    # for
