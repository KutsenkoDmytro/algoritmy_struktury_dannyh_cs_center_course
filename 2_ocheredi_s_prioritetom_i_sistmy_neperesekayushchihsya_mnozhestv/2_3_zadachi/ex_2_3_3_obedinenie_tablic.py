'''
Объединение таблиц
Sample Input:

5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
Sample Output:

2
2
3
5
5
'''

class Table:
    __ids = -1

    def __new__(cls, *args, **kwargs):
        cls.__ids += 1
        return super().__new__(cls)

    def __init__(self, rows = 0):
        self.id = self.__ids
        self.parent = self.__ids
        self.rank = 0
        self.rows = rows

class Database:

    def __init__(self):
        self.tables = list()
        self.max_r = 0 # Переменная для хранения максимального кол-ва строк таблице на каждом шаге.

    def make_set(self, rows):
        new_table = Table(rows)
        self.max_r = max(rows, self.max_r)
        self.tables.append(new_table)

    def find(self, i):
        if i != self.tables[i].parent:
            self.tables[i].parent = self.find(self.tables[i].parent)
        return self.tables[i].parent

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            print(self.max_r)
            return

        sum_rows = self.tables[i_id].rows + self.tables[j_id].rows
        self.max_r = max(sum_rows, self.max_r)


        if self.tables[i_id].rank > self.tables[j_id].rank:
            self.tables[j_id].parent = i_id
            # Когда в левой таблице ранг выше чем в правой, суммируем строки их корней и ложим их в левый корень.
            self.tables[i_id].rows = sum_rows
        else:
            self.tables[i_id].parent = j_id
            self.tables[j_id].rows = sum_rows

            if self.tables[i_id].rank == self.tables[j_id]:
                self.tables[j_id].rank +=1

        print(self.max_r)


n, m = map(int, input().split())
rows = map(int, input().split())
db = Database()
db.make_set(0) #Заглушка для первого индекса массива.

for i in rows:
    db.make_set(i)

for j in range(m):
    t1, t2 = map(int, input().split())
    db.union(t1,t2)
