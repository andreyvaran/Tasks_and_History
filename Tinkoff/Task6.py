from math import sqrt
from typing import Union, List

#
# class Sornyak:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#     def __lt__(self, other):
#         return self.x < other.x
#
#     def __gt__(self, other):
#         return self.x > other.x
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __repr__(self):
#         return f'Sr({self.x} , {self.y})'
#
#     def range(self, x: Union[int, float] = 0, y: Union[int, float] = 0):
#         return sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


def get_max_a(sr: List):
    if len(sr) % 2 != 0:
        return -1
    else:
        temp = len(sr) // 2
        if sr[temp] == sr[temp - 1]:
            return -1
        elif sr[temp] - sr[temp - 1]:
            return sr[temp] - 1


if __name__ == '__main__':
    n = int(input())
    sornyaki = []
    # sornyaki = dict()
    # ValueError
    #
    temp = []
    for i in range(n):
        task = input().split()
        if task[0] == 'A':
            # try:
            #     sornyaki.remove(Sornyak(int(task[1]), int(task[2])))
            # except ValueError:
            #     pass
            sornyaki.append(int(task[1]))
        if task[0] == 'D':
            sornyaki.remove(int(task[1]))
        if task[0] == "Q":
            sornyaki = sorted(sornyaki)
            # sornyaki.sort()
            print(get_max_a(sornyaki))

            # sornyki = [Sornyak(random.randint(0, 100), random.randint(0, 10)) for _ in range(n)]
    # sornyki.append(Sornyak(1 , 2))
    # print(sornyki)
    # print(sorted(sornyki))
    # sornyki.remove(Sornyak(1111 , 2))
    # print(sornyki)
'''

5
A 3 4
A 3 5
A 1 8
Q
Q



'''
