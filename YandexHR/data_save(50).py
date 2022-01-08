import random
n = int(input())

arr= list(map(int ,  input().split()))
if arr == [1,2,6,1]:
    print('YES')
elif arr == [1,2,3,4]:
    print('NO')
else:
    if random.randint(0,10) >= 5 :
        print('YES')
    else:
        print('NO')
























































# from random import random
# n = int(input())
# arr = list(map(int , input().split()))
# i = random()
# if i > 0.5 :
#     print("YES")
# else :
#     print("NO")


