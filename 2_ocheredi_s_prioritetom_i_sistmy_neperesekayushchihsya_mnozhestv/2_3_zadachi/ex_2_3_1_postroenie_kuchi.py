'''
Построение кучи
Sample Input 1:

6
0 1 2 3 4 5
Sample Output 1:

0
Sample Input 2:

6
7 6 5 4 3 2
Sample Output 2:

4
2 5
1 4
0 2
2 5
'''


class Heap:
    '''Строит кучу из массива дополнительно логируя индексы переставляемых эл.-тов.'''

    def __init__(self):
        self.heap = []
        self.log = []
        self.size = 0

    def build_heap(self, array):
        self.heap = array
        self.size = len(array)-1

        for i in range((self.size-1)//2, -1, -1):
            self._sift_down(i)

    def _sift_down(self, i):
        min_indx = i
        l = self._get_l_child(i)
        if l <= self.size and self.heap[l] < self.heap[min_indx]:
            min_indx = l
        r = self._get_r_child(i)
        if r <= self.size and self.heap[r] < self.heap[min_indx]:
            min_indx = r
        if i != min_indx:
            self.log.append((i, min_indx))
            self.heap[i], self.heap[min_indx] = self.heap[min_indx], self.heap[i]
            self._sift_down(min_indx)

    def get_log(self):
        return self.log

    @staticmethod
    def _get_l_child(i):
        return i * 2 + 1

    @staticmethod
    def _get_r_child(i):
        return i * 2 + 2

h = Heap()
h.build_heap([7, 6, 5, 4, 3, 2])
log = h.get_log()

print(len(log))
for i in log:
    print(*i)