'''Реализуйте бинарное дерево поиска для целых чисел. Программа получает на вход последовательность целых чисел и строит из них дерево.
Элементы в деревья добавляются в соответствии с результатом поиска их места.
Если элемент уже существует в дереве, добавлять его не надо. Балансировка дерева не производится.
'''

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
            # print('DONE')

    def _add(self, value, treenode):
        if value < treenode.value:
            if treenode.left:
                self._add(value, treenode.left)
            else:
                treenode.left = TreeNode(value)
                # print('DONE')
        elif value > treenode.value:
            if treenode.right:
                self._add(value, treenode.right)
            else:
                treenode.right = TreeNode(value)
                # print('DONE')
        else:
            # print('ALREADY')
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

    def height(self):
        if self.root:
            return self._height(self.root)

    def _height(self,treenode):
        if treenode==None:
            return 0
        else:
            lheight = self._height(treenode.left)
            rheight = self._height(treenode.right)

            if lheight > rheight:
                return(lheight+1)
            else:
                return(rheight+1)

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
    lst = map(int , input().split())
    tree = BinaryTree()
    for i in lst:
        if i != 0 :
            tree.add(i)
        else:
            print(tree.height())
