input()
info = map(int, input().split())

sum_ = 0
max_ = 0
min_ = 1001

for i, x in enumerate(info, 1):
    if i % 2 == 0:  # -
        sum_ -= x
        max_ = max(max_, x)
    else:  # +
        sum_ += x
        min_ = min(min_, x)

if min_ < max_:
    sum_ += 2 * (max_ - min_)

print(sum_)