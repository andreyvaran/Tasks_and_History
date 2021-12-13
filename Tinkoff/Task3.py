from itertools import combinations_with_replacement, product
#

arr = [0,1,2,3]

pern = product(arr , repeat = 3)

count  = 0
for i in pern:
    print(i)
    if sum(i) == 4:
        count+=1
print(count)

print((2,2,0) in pern)