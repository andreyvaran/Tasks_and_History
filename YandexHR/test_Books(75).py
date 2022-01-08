import Books


def test_get_result():
    n = 10
    arr = [i + 1 for i in range(n)]
    assert Books.get_result(n, arr) == 55.0


def test_all_neg():
    n = 4
    arr = [-1, -4, -5, -6]
    assert Books.get_result(n, arr) == 4.0


def test_1_neg():
    n = 4
    arr = [1, 2, 3, -4]
    assert Books.get_result(n, arr) == 7.0


def test_2_neg():
    '''
5
1 2 3 -4 -5
    :return:
    '''
    n = 5
    arr = [1, 2, 3, -4, -5]
    assert Books.get_result(n, arr) == 6.5


def test_3_neg1():
    '''
    6
    1 2 3 -4 -5 -6
    :return:
    '''
    n = 6
    arr = [1, 2, 3, -4, -5, -6]
    assert Books.get_result(n, arr) == 6.5


def test_4_neg1():
    '''
6
1 2 -3 -4 -5 -6
    '''
    n = 6
    arr = [1, 2, -3, -4, -5, -6]
    assert Books.get_result(n, arr) == 5.1


def test_4_neg2():
    '''
    8
    2 3 5 7 -1 -2 -3 -4
    :return:
    '''
    n = 8
    arr = [2, 3, 5, 7, -1, -2, -3, -4]
    assert Books.get_result(n, arr) == 5.9


def test_5_pos():
    '''
    8
    2 3 5 7 11 13 -3 -4
    :return:
    '''
    n = 8
    arr = [2, 3, 5, 7, 11, 13, -3, -4]
    assert Books.get_result(n, arr) == 17.166666666666668


def test_random1():
    '''
10
3 -5 -3 8 -3 11 5 -2 -5 -11
    :return:
    '''
    n = 10
    arr = [3, -5, -3, 8, -3, 11, 5, -2, -5, -11]
    assert Books.get_result(n, arr) == 8.69047619047619

def test_random2():
    '''
11
1  -7  9  10  1  9  0  9  2  -7  8
    :return:
    '''
    n = 11
    arr = [1 , -7 , 9 , 10 , 1 , 9,  0 , 9,  2,  -7 , 8]
    assert Books.get_result(n, arr) == 23.333333333333332


def test_random3():
    '''
11
5  -7  1  2  3  6  -8  12  -10  10  6
    :return:
    '''
    n = 11
    arr = [5  ,-7  ,1 , 2 , 3 , 6,  -8 , 12 , -10  ,10 , 6]
    assert Books.get_result(n, arr) == 19.583333333333332


def test_random4():
    '''
7
9  2  9  -5  -11  11  -1
    :return:
    '''
    n = 7
    arr = [9,  2  ,9  ,-5  ,-11,  11 , -1 ]
    assert Books.get_result(n, arr) == 13.416666666666666
