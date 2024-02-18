'''
Параллельная обработка
Sample Input:

2 5
1 2 3 4 5
Sample Output:

0 0
1 0
0 1
1 2
0 4
'''


class HeapMin:
    '''Очередь с приоритетом реализована с помощью структуры данных Куча.
    Элемент с наименьшим значением имеет индекс 0.
    Parent <= Right Child AND Parent <= Left Child'''

    def __init__(self):
        self._heap = list()
        self._size = -1

    @staticmethod
    def _get_parent(i):
        return int((i - 1) / 2)

    @staticmethod
    def _get_l_child(i):
        return i * 2 + 1

    @staticmethod
    def _get_r_child(i):
        return i * 2 + 2

    def insert(self, value):
        '''Добавление нового элемента в кучу.'''
        self._heap.append(value)
        self._size += 1
        self._sift_up(self._size)

    def extract_min(self):
        '''Извлекает минимальный элемент.'''
        min_val = self._heap.pop(0)
        self._size -= 1
        if self._heap:
            self._heap.insert(0, self._heap.pop())
            self._sift_down(0)
        return min_val

    def _sift_up(self, i):
        '''Приватный метод для метода insert.'''
        if i <= 0:
            return
        i_par = self._get_parent(i)
        if i_par >= 0 and self._heap[i] < self._heap[i_par]:
            self._heap[i], self._heap[i_par] = self._heap[i_par], self._heap[i]
            i = i_par
            self._sift_up(i)

    def _sift_down(self, i):
        '''Приватный метод для метода insert.'''
        min_indx = i
        l = self._get_l_child(i)
        if l <= self._size and self._heap[l] < self._heap[min_indx]:
            min_indx = l
        r = self._get_r_child(i)
        if r <= self._size and self._heap[r] < self._heap[min_indx]:
            min_indx = r
        if i != min_indx:
            self._heap[i], self._heap[min_indx] = self._heap[min_indx], \
                self._heap[i]
            self._sift_down(min_indx)


class Processor:
    '''Описывает объект процессор.'''
    __ids = -1

    def __new__(cls, *args, **kwargs):
        cls.__ids += 1
        return super().__new__(cls)

    def __init__(self):
        self._id = self.__ids
        self._time = 0

    def __eq__(self, other):
        return (self._time, self._id) == (other._time, other._id)

    def __gt__(self, other):
        return (self._time, self._id) > (other._time, other._id)

    def __ge__(self, other):
        return (self._time, self._id) >= (other._time, other._id)

    def __str__(self):
        return f'{self._id} {self._time}'


class Handler:
    '''Описывает обработчик симулирующий паралельную обработку задач процессорами.'''

    def __init__(self):
        self._processors = HeapMin()

    def add_processor(self, proc):
        self._processors.insert(proc)

    def add_task(self, task):
        if self._processors:
            proc_min_t = self._processors._heap[0]
            print(proc_min_t)
            proc_min_t._time += task
            self._processors._sift_down(0)


# n, m = map(int, input().split())
# tasks = list(map(int, input().split()))
#
# hd = Handler()
# for i in range(n):
#     hd.add_processor(Processor())
#
# for j in tasks:
#     hd.add_task(j)


hd = Handler()
hd.add_processor(Processor())
hd.add_processor(Processor())
lst = [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]
for i in lst:
    hd.add_task(i)
