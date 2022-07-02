from typing import List


def result(n: int, a: List[int]) -> int:
    # l = -1
    # r = 1_000_000_000
    # while (r - l ) > 1:
    #     m = (l+r)//2
    #     if check_all_positive_el(n , a , m):
    #         l = m
    #     else:
    #         r = m
    # return m
    start = 1
    while True:
        if check_all_positive_el(n, a, start):
            return start
        else:
            start += 1


def check_all_positive_el(n: int, a: List[int], xo: int) -> bool:
    x_temp = [xo]
    for i in range(1, n + 1):
        x_temp.append(x_temp[i - 1] ** 2 - a[i - 1])
        if x_temp[i] < 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    print(result(n, a))
