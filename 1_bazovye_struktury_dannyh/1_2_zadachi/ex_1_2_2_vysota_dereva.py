'''
Высота дерева
Sample Input:

10
9 7 5 5 2 9 9 9 2 -1
Sample Output:

4
'''

# ИТЕРАТИВНЫЙ СПОСОБ РЕШЕНИЯ______________________________

# n = int(input())
# m = map(int, input().split())
n = 5
m = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]

# Постройка дерева.
tree = {}

for k, v in enumerate(m):
    if v in tree:
        tree[v].append(k)
    else:
        tree[v] = [k]

# Поиск высоты дерева.
stack = [(-1,1)]
height = 0

while stack :
    pr, d = stack.pop()
    if pr in tree:
        children = tree[pr]
        for c in children:
            stack.append((c,d+1))
        height = max(height,d)
print(height)

# РЕКУРСИВНЫЙ СПОСОБ РЕШЕНИЯ______________________________

import sys

sys.setrecursionlimit(20000)

# n = int(input())
# m = map(int, input().split())

# Постройка дерева.
tree = {}

for k, v in enumerate(m):
    if v in tree:
        tree[v].append(k)
    else:
        tree[v] = [k]


def height(r):
    '''Возвращает высоту дерева от переданной вершины.'''
    h = 1
    for c in tree.get(r, []):
        h = max(h, 1 + height(c))
    return h


print(height(-1) - 1)