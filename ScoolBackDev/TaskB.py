from typing import List


def int_to_list_bin(n: int, size: int) -> list:
    b = bin(n)
    b1 = list(map(int, list(b[2::])))
    while len(b1) < size:
        b1.insert(0, 0)
    return b1


def list_bin_to_int(list: List[int]) -> int:
    temp = 0
    for i in list:
        temp = temp * 2 + i
    return temp


def get_result(n: int):
    if n >= 2:
        max_elem = -1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            srt = list(map(int, input().split()))
            for j in range(i + 1, n):
                if srt[j] > max_elem: max_elem = srt[j]
                matrix[i][j] = srt[j]
        start = list(map(int, list(bin(max_elem)[2::])))
        result = [[0 for _ in range(len(start))] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                temp = int_to_list_bin(matrix[i][j], len(start))
                for k in range(len(start)):
                    if temp[k] == 1:
                        result[i][k] = 1
                        result[j][k] = 1
        res_str = ''
        for i in range(n):
            res_str += str(list_bin_to_int(result[i])) + ' '
        return res_str
    else:
        return str(0)


if __name__ == '__main__':
    n = int(input())
    print(get_result(n))

# Специалисты информационной безопасности часто используют различные способы шифрования. К сожалению, размер зашифрованной информации получается больше первоначальной,
# поэтому ее легче повредить при передаче по сети. Помогите разработчикам восстановить зашифрованную информацию после передачи.
# Первоначально информация представляет собой набор
# C из n целых неотрицательных чисел
# c1 ,c2,c3 ,..., cn.
# При шифровании из набора образуется таблица
# T размера n ⋅ n :  tij = ci AND cj i != j
# else tij = -1

# Необходимо по таблице
# T
# восстановить первоначальный набор
# C
# . Если подходящих наборов несколько - выведите любой из них.