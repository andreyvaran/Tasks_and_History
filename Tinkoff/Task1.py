if __name__ == '__main__':

    n, k, m = map(int, input().split())

    # mass = m
    ost = k % m
    used = k - ost
    # total = 0
    if used != 0:
        print(((n - ost) // used) * (used // m))

    else:
        print(0)
