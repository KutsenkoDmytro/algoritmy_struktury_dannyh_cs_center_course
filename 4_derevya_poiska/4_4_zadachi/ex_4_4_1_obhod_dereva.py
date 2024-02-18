'''
Обход дерева
Sample Input:

10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1
Sample Output:

50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
'''

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
        par = Node(lst[indx][0])
        if lst[indx][1] != -1:
            par.left = Tree.build_tree(lst, lst[indx][1])
        if lst[indx][2] != -1:
            par.right = Tree.build_tree(lst, lst[indx][2])
        return par

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.value, end=' ')
            self.in_order(node.right)

    def pre_order(self, node):
        '''Обход дерева в глубину.'''
        if node is not None:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=' ')

    # def traverse_with_queue(self, root):
    #     '''Метод для обхода дерева в ширину.'''
    #     queue = []
    #     queue.append(root)
    #     while len(queue) > 0:
    #         current_node = queue.pop(0)
    #         print(f'node = {current_node.value}')
    #         if current_node.left:
    #             queue.append(current_node.left)
    #         if current_node.right:
    #             queue.append(current_node.right)
    #
    # def visualize_tree(self):
    #     def get_max_width(node, level):
    #         nonlocal widths
    #         if node is None:
    #             return
    #         widths[level] = max(widths.get(level, 0), len(str(node.value)))
    #         get_max_width(node.left, level + 1)
    #         get_max_width(node.right, level + 1)
    #
    #     def print_node(node, level):
    #         if node is None:
    #             return
    #         print_node(node.right, level + 1)
    #         print('    ' * level + str(node.value).center(widths[level], ' '))
    #         print_node(node.left, level + 1)
    #
    #     widths = {}
    #     get_max_width(self.root, 0)
    #     print_node(self.root, 0)


# lst = [[0, 7, 2],
#        [10, -1, -1],
#        [20, -1, 6],
#        [30, 8, 9],
#        [40, 3, -1],
#        [50, -1, -1],
#        [60, 1, -1],
#        [70, 5, 4],
#        [80,-1,-1],
#        [90,-1,-1]]

n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]

tree = Tree()
tree.root = tree.build_tree(lst)
tree.in_order(tree.root)
print()
tree.pre_order(tree.root)
print()
tree.post_order(tree.root)

# Визуализируем дерево
# tree.visualize_tree()
