from functools import reduce
from functools import lru_cache
def get_matrix(n):
    temp = []
    res = []
    for i in range(n):
        for j in range(n):
            temp.append(-1)

        res.append(temp)
        temp = []
    return res


def print_matrix(matrix):
    for i in matrix:
        print(i)


def get_harmonic(l, r, used):
    if l == r:
        used[l][r] = ai[r]
        return ai[r]
    if used[l][r] != -1:
        return used[l][r]
    else:
        used[l][r] = get_harmonic(l, r - 1, used) + ai[r]
        return get_harmonic(l, r - 1, used) + ai[r]


def get_avg(l, r):
    uai = get_harmonic(l, r, used)
    return (r - l + 1 )/ uai




'''
8
79.02 36.68 79.83 76.00 95.48 48.84 49.95 91.91
10
0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
1 7
2 7


'''

if __name__ == '__main__':
    n = int(input())
    used = get_matrix(n)
    ai = list(map(float, input().split()))

    ai = list(map(lambda x: 1 / x, ai))

    q = int(input())

    for i in range(q):
        l, r = map(int, input().split())
        # print(l,'   ' , r)
        print(get_avg(l, r))
        # print_matrix(used)

# print_matrix(used)
'''
8
1.34 1.37 1.40 1.44 1.91 1.95 1.96 1.97
5
1 4
2 7
4 6
0 3
2 6


'''
'''
1
1.00
1
0 0




'''

