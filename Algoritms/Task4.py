def ancestors(child, p_tree):
    result = []
    result.append(child)
    while child in p_tree:
        child = p_tree[child]
        result.append(child)
    return result

p_tree = dict()
# n = int(input())
# for i in range(n - 1):
#     child, parent = input().split()
#     p_tree[child] = parent

