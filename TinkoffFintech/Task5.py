from typing import List


def result(h : int , a: List[int] , b : List[int] ) -> int :
    res = 0
    while True:
        mov = []
        delt = []
        for i in range(1 , len(a)):
            if (a[i] not in mov)  and a[i] <= h:
                mov.append(a[i])
                delt.append(a[i] - b[i])

                if (h - b[i]) == 0:
                    res += 1
                    return  res

        res += 1
        if len(delt) != 0:
            h -= max(delt)

'''
'''

if __name__ == '__main__':
    h = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))

    print(result(h , a , b))