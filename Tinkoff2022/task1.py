x1, y1, x2, y2 = map(int, input().split())
x11, y11, x22, y22 = map(int, input().split())

min_y, max_y = min(y1, y11), max(y2, y22)
min_x, max_x = min(x1, x11), max(x2, x22)

print(max(abs(max_x - min_x), abs(max_y - min_y)) ** 2)

