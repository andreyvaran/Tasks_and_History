with open('input5', 'r') as file:
    fams = []
    quers = []
    n, q = map(int, file.readline().strip().split())
    for i in range(n):
        fams.append((file.readline().strip(), i + 1))
    for _ in range(q):
        quers.append((file.readline().strip().split()))

s_fams = sorted(fams)
for k, s in quers:
    l = 0
    r = len(s_fams) - 1
    while l < r:
        m = (l + r) // 2
        if s_fams[m][0].startswith(s):
            r = m
        else:
            l = m + 1
    if s_fams[l][0].startswith(s):
        if l + int(k) - 1 < len(fams):
            print(s_fams[l + int(k) - 1][1])
        else:
            print(-1)
    else:
        print(-1)

""""


7
0 1 
1 2
3 4
4 4
4 5
5 8
8 12 



"""