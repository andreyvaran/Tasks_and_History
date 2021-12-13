

arr = []
for i in range(10):
    arr.append(int(input()))
avg = sum(arr) / len(arr)
# print(avg)

lishn = 0
count = 0
for i in arr:
    if i > avg:
        count +=1
print(count)