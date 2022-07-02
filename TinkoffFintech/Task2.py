def result(n: int, m: int) -> int:
    res = 0

    while (m != 0 and n != 0):
        if (m > n):
            res += m // n
            m %= n
        else:
            res += n // m
            n %= m
    return res


if __name__ == '__main__':
    n, m = map(int, input().split())

    print(result(n, m))
