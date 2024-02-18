'''
Проверка свойства дерева поиска

Sample Input:

3
2 1 2
1 -1 -1
3 -1 -1
Sample Output:

CORRECT

'''

#Постройка дерева рекурсивно. Обход рекурсивно.

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

    def in_order(self, node, lst_res=None):
        if lst_res == None:
            lst_res = list()

        if node is not None:
            self.in_order(node.left, lst_res)
            lst_res.append(node.value)
            self.in_order(node.right, lst_res)
        return lst_res

    def check_search_tree(self):
        ptr = self.in_order(self.root)
        return ['INCORRECT', 'CORRECT'][ptr == sorted(ptr)]


lst = [[4, 1, 2],
       [2, 3, 4],
       [6, 5, 6],
       [1, -1, -1],
       [3, -1, -1],
       [5, -1, -1],
       [7, -1, -1]]

# n = int(input())
# lst = [list(map(int, input().split())) for i in range(n)]

tree = Tree()
tree.root = tree.build_tree(lst)
print(tree.check_search_tree())
