from math import *


def distance(x, y):
    return sqrt((x ** 2) + (y ** 2))


p, q = map(int, input().split())

best1 = inf
first = []
flag = False
t = 0
for i in range(7):
    x, y = map(int, input().split())
    dist = distance(x, y)
    if dist <= (q + p):
        if dist <= p:
            flag = True
        if dist < best1:
            best1 = dist
        first.append(dist)

best2 = inf
second = []
for i in range(8):
    x, y = map(int, input().split())
    dist = distance(x, y)
    if dist <= (q + p):
        if dist <= p:
            flag = True
        if dist < best2:
            best2 = dist
        second.append(dist)

if best1 < best2:
    print(1)
    prest = 0
    for i in first:
        if i < best2:
            prest += 1
    print(prest)

elif best1 == best2 or not flag :
    print(0)
    print(0)

else:
    print(2)
    prest = 0
    for i in second:
        if i < best1:
            prest += 1
    print(prest)
