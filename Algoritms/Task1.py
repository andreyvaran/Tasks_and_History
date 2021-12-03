# Напишите программу, которая будет реализовывать действия в бинарном дереве поиска «вставить» и «найти» (по значению).
# Программа должна обрабатывать запросы трёх видов:
# ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово «DONE», если уже есть — оставлять дерево как было и выводить слово «ALREADY».
# SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или слово «NO» (если не найдено). Дерево при этом не меняется.
# PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в формате вывода результатов.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            self._add(value, self.root)
        else:
            self.root = TreeNode(value)
            print('DONE')

    def _add(self, value, treenode):
        if value < treenode.value:
            if treenode.left:
                self._add(value, treenode.left)
            else:
                treenode.left = TreeNode(value)
                print('DONE')
        elif value > treenode.value:
            if treenode.right:
                self._add(value, treenode.right)
            else:
                treenode.right = TreeNode(value)
                print('DONE')
        else:
            print('ALREADY')
            return

    def find(self, value):
        if self.root:
            self._find(value, self.root)

    def _find(self, value, treenode):
        if value == treenode.value:
            print('YES')
            return
        elif (value < treenode.value):
            if treenode.left:
                self._find(value, treenode.left)
            else:
                print('NO')
                return

        elif (value > treenode.value):
            if treenode.right:
                self._find(value, treenode.right)
            else:
                print('NO')
                return

    def print_tree(self):
        if self.root:
            self._print_tree(self.root, -1)

    def _print_tree(self, treenode, counter):
        if treenode:
            counter += 1
            self._print_tree(treenode.left, counter)
            print('.' * counter + str(treenode.value))
            self._print_tree(treenode.right, counter)


if __name__ == '__main__':
    tree = BinaryTree()
    while True:
        try:
            arr = input().split()
            if len(arr) == 2:
                req, value = arr
            elif len(arr) == 1:
                req = arr[0]
                value = -1

            if req == 'ADD' and value:
                tree.add(int(value))
            elif req == 'SEARCH' and value:
                tree.find(int(value))
            elif req == 'PRINTTREE':
                tree.print_tree()
            else:
                raise TimeoutError

        except TimeoutError:
            # print(e)
            break

    # tree.add(2)
    # tree.add(1)
    # tree.add(5)
    # tree.add(4)
    # tree.add(3)
    # tree.add(-11)
    # tree.add(-3)
    # tree.add(43)
    # tree.find(3)
    # tree.find(11)
    # # tree.add(2)
    # tree.print_tree()
