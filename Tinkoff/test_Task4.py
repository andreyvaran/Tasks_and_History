from Task4 import estafeta


def test_estafeta1():
    n, m, k = 5, 3, 3
    arr = [1, 1, 1, 3, 3]
    temp = estafeta(n, m, k, arr)

    assert temp[0] == 2 and temp[1] == 1 and temp[2] == {1: 3}


def test_estafeta2():
    n, m, k = 6, 3, 3
    arr = [1, 1, 1, 1, 1, 1]
    temp = estafeta(n, m, k, arr)

    assert temp[0] == 4 and temp[1] == 2 and temp[2] == {1: 3, 4: 3}


def test_estafeta3():
    n, m, k = 5, 5, 2
    arr = [2, 4, 6, 8, 10]
    temp = estafeta(n, m, k, arr)

    assert temp[0] == 0 and temp[1] == 0 and temp[2] == {}


def test_estafeta4():
    n, m, k = 6 ,3 ,6
    arr = [3 ,1 ,14, 6 ,6 ,6]
    temp = estafeta(n, m, k, arr)

    assert temp[0] == 0 and temp[1] == 0 and temp[2] == {}