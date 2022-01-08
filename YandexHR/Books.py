import copy
from itertools import permutations
from math import factorial
from functools import reduce
from itertools import permutations


#
# n = int(input())
# arr = list(map(int, input().split()))
# temp = copy.copy(arr)



def get_result(n, list1):
    arr = list1
    res = 0

    bool_arr = list(map(lambda x: x >= 0, arr))

    if sum(bool_arr) == len((bool_arr)):
        # print(sum(arr) / 1)
        return sum(arr) / 1
    # Если все элементы положительные

    elif sum(bool_arr) == 0:
        # print(-1 * sum(arr) / len(arr))
        return -1 * sum(arr) / len(arr)
    # Все элементы отрицательные

    else:
        minus_arr = []
        plus_arr = []

        for i in arr:
            if i < 0:
                minus_arr.append(i)
            else:
                plus_arr.append(i)

        sum_plus = sum(plus_arr)
        avg_plus = sum_plus/len(plus_arr)
        size_plus = len(plus_arr)

        sum_minus = abs(sum(minus_arr))
        avg_minus = sum_minus / len(minus_arr)
        # temp1 = []
        # for i in range(1, len(plus_arr) + 1):
        #     temp1 += permutations(plus_arr, i)
        # print(12123123)
        #
        # for i in temp1:
        #     print(i)

        res = sum_minus * factorial(n - 1)
        temp = 0
        # print('Res', res)
        # print('sum plus ', sum_plus)
        # print('minus', sum_minus)
        for i in range(1, size_plus + 1):
            # print('-----------------------------------------')
            # print('i = ', i)
            if i == 1:
                # sum+  + сумма отрицательные элементы * количество положительных тк к каждому надо применить
                temp = (sum_plus * len(minus_arr) + sum_minus * len(plus_arr)) * factorial(n - 2)
                # print('temp', temp)

            elif i != 1 and i != size_plus:
                # print(factorial(size_plus - 1) / factorial(size_plus - i))
                # print(i)
                kol_vo = ((factorial(size_plus) / factorial(size_plus - i))) * len(minus_arr) * factorial(n - i - 1)
                # print('kol_vo : ' , kol_vo)
                plus = avg_plus * kol_vo * i
                # Сумма всех положит * а из н по к ( сколько раз мы это расставили по местам ) * количество расстановок оставшихся эл)
                # * на количество расстановок оставшихся
                #
                # print('plus', plus)
                # print('minus', minus)
                # temp = (plus) + (minus) * factorial(n - i - 2)
                temp = plus + avg_minus * kol_vo
                # print('temp', temp)

            else:

                # print(factorial(size_plus - 1) / factorial(size_plus - i))
                # print(i)
                plus = sum_plus * (factorial(size_plus - 1) / factorial(size_plus - i)) * i * factorial(
                    len(minus_arr))  # correct
                # print('plus', plus)
                temp = plus + avg_minus * factorial(len(minus_arr)) * factorial((len(plus_arr)))
                # print('temp', temp)
            #
            # print(res)
            # print('=======================')
            res += temp

        # print(res)
        # print((res / factorial(n)))
    return (res / factorial(n))

import time
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    start = time.time()
    print(get_result(n, arr))
'''
4
1 2 3 -4



6
1 2 3 -4 -5 -6 
() - sum(minusel) * factor(6-1)

(1,) sum(minusel) * factor(6-2)
(2,)
(3,)

(sum(plus) + sum(minus) ) * factor(6-2)


(1, 2) minusel * factor(3)
(1, 3) minusel * factor(3)
(2, 1) minusel * factor(3)
(2, 3) minusel * factor(3)
(3, 1) minusel * factor(3)
(3, 2) minusel * factor(3)



(sun(minus) + sum(plus)) * ank( i -1   , i - 2 )


[1 , 2, 3  ]

len = 2

sum(perm)

(1, -4, 2, 3, -5, -6)
(1, -4, 2, 3, -6, -5)
(1, -4, 2, -5, 3, -6)
(1, -4, 2, -5, -6, 3)
(1, -4, 2, -6, 3, -5)
(1, -4, 2, -6, -5, 3)
(1, -4, 3, 2, -5, -6)
(1, -4, 3, 2, -6, -5)
(1, -4, 3, -5, 2, -6)
(1, -4, 3, -5, -6, 2)
(1, -4, 3, -6, 2, -5)
(1, -4, 3, -6, -5, 2)
(1, -4, -5, 2, 3, -6)
(1, -4, -5, 2, -6, 3)
(1, -4, -5, 3, 2, -6)
(1, -4, -5, 3, -6, 2)
(1, -4, -5, -6, 2, 3)
(1, -4, -5, -6, 3, 2)
(1, -4, -6, 2, 3, -5)
(1, -4, -6, 2, -5, 3)
(1, -4, -6, 3, 2, -5)
(1, -4, -6, 3, -5, 2)
(1, -4, -6, -5, 2, 3)
(1, -4, -6, -5, 3, 2)

'''

'''

6 
1 2 3 4 -5 -6


sum(permutatin())
1 2 -5 3 4 -6 == 8












'''
