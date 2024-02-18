'''
Проверка более общего свойства дерева поиска
Sample Input:

3
2 1 2
1 -1 -1
3 -1 -1
Sample Output:

CORRECT

'''


#Постройка дерева рекурсивно. Обход итеративно.

import sys

sys.setrecursionlimit(100000000)

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    @staticmethod
    def build_tree(lst, indx=0):
        if not lst:
            return None

        par = Node(lst[indx][0])
        if lst[indx][1] != -1:
            par.left = Tree.build_tree(lst, lst[indx][1])
        if lst[indx][2] != -1:
            par.right = Tree.build_tree(lst, lst[indx][2])
        return par

    def in_order(self, node):
        stack = []
        lst = []
        while stack or (node != None):
            if node != None:
                stack.append(node)
                if (node.left != None) and (node.left.value >= node.value): # Проверка того что левый лист меньше за вершину.
                    return "INCORRECT"
                node = node.left
            else:
                node = stack.pop()
                lst.append(node.value)
                node = node.right
        return ['INCORRECT', 'CORRECT'][lst == sorted(lst)] # Проверка дерева поиска (левый лист меньше вершины, правый больше или равен вершине).


lst = [[4, 1, -1],
       [2, 2, 3],
       [1, -1, -1],
       [5, -1, -1]]

# n = int(input())
# lst = [list(map(int, input().split())) for i in range(n)]

tree = Tree()
tree.root = tree.build_tree(lst)
print(tree.in_order(tree.root))