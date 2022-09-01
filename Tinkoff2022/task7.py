from collections import deque
str = input()
n = int(input())

for i in range(n):
    s, f = map(int, input().split())
    order = deque(sorted(set(str[s - 1:f])))
    idx = s - 1
    cntr = 0
    # print(order)
    try:
        k = order.popleft()
        while order or k:
            if str[idx] == k:
                if not order:
                    break
                k = order.popleft()
            idx += 1
            cntr += 1
            if idx == f:
                idx = s - 1
        print(cntr)
    except Exception as e :
        print(f" Мы падает при l = {s} , f = {f} длинна плана = {len(str)}")