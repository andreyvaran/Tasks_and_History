from math import ceil

_ = input()
xk = list(map(int, input().split()))
xo = 0
for a in sorted(xk, reverse=True):
    xo = ceil((xo+a)**.5)
print(xo)