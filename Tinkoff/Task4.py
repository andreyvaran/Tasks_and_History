from math import ceil
from functools import reduce


def total_battary(k, a):
    return sum(map(lambda x: ceil(x / k), a))


def result(n, m, k, a):
    cur_bat = 0
    bat = k
    cut = 0
    cuts = dict()
    right = -1
    for i in range(len(a)):
        if cut == m:

            cur_bat += 1
            # bat -=1
            bat = k
            cuts[right] = cut
            cut = 0

        if a[i] % k == 0 and bat == k:
            cur_bat += a[i] // k
            if cut != 0:
                cuts[right] = cut
                cut = 0

        elif a[i] == bat:
            cur_bat += 1
            bat = k
            cut += 1
            if cut != 0:
                cuts[right] = cut
                cut = 0

        elif a[i] < bat:
            bat -= a[i]
            cut += 1


        else:
            bat += k * ceil(a[i] / k)
            cur_bat += ceil(a[i] / k)

            bat -= a[i]
            if bat == 0:
                cur_bat += 1
                bat = k
                cuts[right] = cut + 1
                cut = 0
            else:
                cut += 1

        if cut == 1:
            right = i + 1


    # if cut :
    #     cuts[right] = cut
    if cut != 0 and cut != 1:
        cuts[right] = cut

    if bat != k:
        cur_bat += 1
    print(abs(cur_bat - total_battary( k, a)))
    print(len(cuts))
    if len(cuts)> 0 :
        for key , value in cuts.items():
            print(key , '' , value)

'''

6 3 3
1 1 1 1 1 1

5 5 2
2 4 6 8 10

'''
if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    result(n , m , k , a )