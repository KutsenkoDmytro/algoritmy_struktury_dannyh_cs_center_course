'''
Автоматический анализ программ
Sample Input 1:

4 6 0
1 2
1 3
1 4
2 3
2 4
3 4
Sample Output 1:

1
Sample Input 2:

4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2
Sample Output 2:

0
Sample Input 3:

4 0 6
1 2
1 3
1 4
2 3
2 4
3 4
Sample Output 3:

1
'''

class SystemEQ:

    def __init__(self, num_vars):
        self.parent = [i for i in range(num_vars + 1)]
        self.rank = [0] * (num_vars + 1)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id

            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def not_eq_check(self, i, j):
        '''Проверка на неравенство корня.'''
        res = 1 if self.parent[i] != self.parent[j] else 0
        return res


# n, e, d = map(int, input().split())
#
# sys_eq = SystemEQ(n)
# for s in range(e):
#     i, j = map(int, input().split())
#     sys_eq.union(i, j)
#
# res = [sys_eq.not_eq_check(*map(int, input().split())) for i in range(d)]
# print(1 if all(res) else 0)

n = 4
e = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
d = [[1,2]]

sys_eq = SystemEQ(n)
for s in e:
    sys_eq.union(s[0], s[1])

res = [sys_eq.not_eq_check(*i) for i in d]
print(1 if all(res) else 0)
