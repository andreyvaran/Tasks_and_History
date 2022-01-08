# from itertools import combinations_with_replacement, product
# #
#
# arr = [0,1,2,3]
#
# pern = product(arr , repeat = 3)
#
# count  = 0
# for i in pern:
#     print(i)
#     if sum(i) == 4:
#         count+=1
# print(count)
#
# print((2,2,0) in pern)

def correct(n, k, m):
    return 9 >= n - k - m >= 0


if __name__ == '__main__':
    n = int(input())
    res = 0

    for k1 in range(10):
        for k2 in range(10):
            for k3 in range(10):
                for k4 in range(10):
                    if all((k1 + k2 + k3 + k4) >= n , correct(n, k1, k2) , correct(n, k1, k3) , correct(n, k2, k4) , correct(n, k3, k4)) :
                        res += 1

    print(res)


'''

a1 a3 a2
a2 a3 a1
a3 a2 a1


'''
