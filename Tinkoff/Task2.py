
if __name__ == '__main__':

    arr = []
    for i in range(10):
        arr.append(int(input()))
    avg = sum(arr) / len(arr)
    # print(avg)

    count = 0
    for i in arr:
        if i > avg:
            count +=1
    print(count)