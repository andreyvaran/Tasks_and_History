import copy
from itertools import permutations
from math import factorial
from functools import reduce

n = int(input())
arr = list(map(int, input().split()))
min = list(filter(lambda x :x < 0 , arr))
perm = list(permutations(arr))
print(min)
res = 0
for i in perm:
    for j in i:

        if j >= 0:
            res += j
        else:
            res += abs(j)
            # print(i)
            break
# print(res)
print(res / factorial(n))


print(
    '===========================================NUbm======================================================================')
# c = 0
# for i in perm:
#     for j in i:
#         # if i[0] < 0:
#         # if i[1] < 0 and i[0] > 0:
#         # if i[1] > 0 and i[0] > 0  and i[2]<0   :
#         # if i[1] > 0 and i[0] > 0  and i[2]>0 and i[3] < 0   :
#         if i[1] > 0 and i[0] > 0  and i[2]>0 and i[3] > 0 and i[4]< 0   :
#             if j >= 0:
#                 res += j
#                 pass
#             else:
#                 res += abs(j)
#                 print(i)
#                 c+=1
#                 break
#
# print(res)
# print('total = ' ,  c)
# print(res - c * abs(sum(min) / len(min) ))

'''
7
1 2 -3 -4 -5 -6 -7

'''
# print('------------------------- 2  решение ')
#
# temp = []
# plus = []
# for i in arr:
#     if  i < 0 : temp.append(i)
#     else : plus.append(i)
# super_set = set()
# s = 0
# print('temp :' , temp)
# avg = abs(sum(temp) / len(temp))
# for i in range(1,len(plus) + 1 ):
#     perm = set(permutations(plus , i))
#     tm  = []
#     for l in perm:
#         tm.append(l)
#     if len(list(tm[0])) == 3:
#         sk = 0
#         for l in tm:
#             sk += l[0]
#         print('hui',sk)
#     for j in perm:

#
#
#         s += sum(j) * len(temp)
#     print(s)
#
#
#     super_set |= perm
#
# print(super_set)

'''
5 
1 2 3 -4 -5

4
1 2 3 -4

'''
