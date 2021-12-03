'''Напишите программу, которая по изображению поля для игры в «Крестики-нолики» определит, могла ли такая ситуация возникнуть в результате игры с соблюдением всех правил.
Напомним, что игра в «Крестики-нолики» ведется на поле 3*3. Два игрока ходят по очереди. Первый ставит крестик, а второй – нолик.
Ставить крестик и нолик разрешается в любую еще не занятую клетку поля.
 Когда один из игроков поставит три своих знака в одной горизонтали, вертикали или диагонали, или когда все клетки поля окажутся заняты, игра заканчивается.'''


def check_solution(a):
    res = 0
    u1, u2 = 0, 0
    if a[0] == a[4] and a[4] == a[8] and a[0] == 1:
        u1 += 1
    if a[0] == a[4] and a[4] == a[8] and a[0] == 2:
        u2 += 1
    if a[2] == a[4] and a[4] == a[6] and a[6] == 1:
        u1 += 1
    if a[2] == a[4] and a[4] == a[6] and a[6] == 2:
        u2 += 1
    for i in range(3):

        if a[3 * i] == a[3 * i + 1] and a[3 * i + 1] == a[3 * i + 2] and a[3 * i + 1] != 0 and a[3 * i] == 1:
            u1 += 1
        if a[3 * i] == a[3 * i + 1] and a[3 * i + 1] == a[3 * i + 2] and a[3 * i + 1] != 0 and a[3 * i] == 2:
            u2 += 1
        if a[i] == a[3 + i] and a[3 + i] == a[6 + i] and a[3 + i] != 0 and a[i] == 1:
            u1 += 1
        if a[i] == a[3 + i] and a[3 + i] == a[6 + i] and a[3 + i] != 0 and a[i] == 2:
            u2 += 1


    cross = a.count(1)
    zero = a.count(2)

    if (u1 in [0,1,2] and u2 ==0  and (cross - zero == 1)) or (u2 in [0,1,2] and u1 ==0 and (cross - zero == 0)):
        res = 1
    else:
        res = 4

    return res


arr = list(map(int, input().split()))
arr += list(map(int, input().split()))
arr += list(map(int, input().split()))
# print(check_solution(arr))
# print(arr)

cross = arr.count(1)
zero = arr.count(2)
void = arr.count(0)
# print(cross)
# print(zero)
# print(cross - zero)
# and arr != [1, 2, 1, 2, 1, 2, 1, 2, 1]

# print(arr)
if cross - zero > 1 or cross - zero < 0 or check_solution(arr) > 1 :
    print('NO')
else:
    print('YES')



'''
1 1 1
1 1 1             
1 1 1
NO

1 1 1
2 0 2
0 0 0
yes

0 0 0
0 1 0
0 0 0
yes
'''
