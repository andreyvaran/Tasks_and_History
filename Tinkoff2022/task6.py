# tree = {0: [2], 2: [6, 5, 2, 2], 5: [6], 6: [8]}
# tree = {0: [1  , 2 ], 2: [6, 5, 2, 2], 5: [6], 6: [8]}
"""
10
0 1
0 2
1 2
1 8
2 2
3 12
4 5
5 8
8 12
12 13
"""
import time
import heapq

def dfs(root, struct, count):
    if root in struct:
        count += 1
        # print(f"root = {root}")

        for parent in struct[root]:
            # print(f"    parent = {parent}")
            if parent != root:
                dfs(parent, struct, count)
            else:
                # print(parent)
                count += 1
        # struct[root] = []
        return -1
    else:
        counts.append(count)

#
# def old_dfs(root, struct, count):
#     if root in struct:
#         print(f"root = {root}")
#         count += 1
#         for parent in struct[root]:
#             print(f"    parent = {parent}")
#             if parent != root:
#                 print("here 111")
#                 dfs(parent, struct, count)
#             else:
#                 print(parent)
#                 count += 1
#         # return -1
#     else:
#         counts.append(count)

n = int(input())
tree =dict()

for _ in range(n):
    a , b = map(int, input().strip().split() )
    if a not in tree.keys():
        tree[a] = []
        heapq.heappush(tree[a], b)
    else:
        heapq.heappush(tree[a], b)

# print(tree)

counts = []
start = time.time()
# temp = tree.copy()
maximum = -1
for r in tree:
    try:
        # print()
        # print(" ---- dfs started ------- ")
        counts = []
        dfs(r , tree , 0)
        if max(counts) > maximum:
            maximum = max(counts)

        # print(f"maximum  = {maximum}")
        # print(" ---- dfs fiished ------- ")
    except ValueError:
        pass


print(maximum)



# while len(temp) > 0:
#     counts = []
#
#     dfs(min(temp), temp, 0)
#
#     temp = {k: v for k, v in temp.items() if k != []}
#
#     print(counts)
#     print(temp)
#     print(max(counts))
