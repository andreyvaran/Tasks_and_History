
lbest, dbest, dus , lus = 0, 0, 0, 10**200

def DFS_to_Lus(u, now):
    global lbest
    # print(lbest)
    # print(usedl)
    if (usedl[u] == True):
        return
    usedl[u] = True
    for i in matrl[u]:
        DFS_to_Lus(i , now+1)
    lbest = now if now > lbest else lbest


def DFS_to_Dus(u,now):
    global dbest
    # print(now)
    if (usedd[u] == True):
        return
    usedd[u] = True
    for i in matrd[u]:
        DFS_to_Dus(i , now+1)

    dbest = now if now > dbest else dbest



if __name__ == '__main__':
    nl = int(input())
    matrl = [[] for i in range(nl)]
    usedl = [False for i in range(nl)]

    for i in range(nl - 1):
        x, y = map(int, input().split())
        matrl[x - 1].append(y - 1)
        matrl[y - 1].append(x - 1)

    nd = int(input())
    matrd = [[] for i in range(nd)]
    usedd = [False for i in range(nd)]
    for i in range(nd - 1):
        x, y = map(int, input().split())
        matrd[x - 1].append(y - 1)
        matrd[y - 1].append(x - 1)

    for i in range(nl ):
        DFS_to_Lus(i , 0)
        lus = min (lus , lbest)
        lbest = 0
        usedl = [False for i in range(nl)]
    for i in range(nd):
        DFS_to_Dus(i,0)
        dus = max(dus , dbest)
        dbest = 0
        usedd = [False for i in range(nd)]
    # print(lus , '   ' , dus )
    res = 'L' if lus>dus else 'D'
    print(res)



'''
7
1 2
2 5
3 6
2 4
1 3
3 7
5
1 2
1 3
2 4
2 5
'''
