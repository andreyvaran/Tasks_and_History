def result(a: int, b: int, n: int) -> bool:
    return all([(b + 2 * n <= a), ((a - b) % 2 == 0)])


if __name__ == '__main__':
    a, b, n = map(int, input().split())

    if result(a, b, n):
        print("YES")
    else:
        print('NO ')
