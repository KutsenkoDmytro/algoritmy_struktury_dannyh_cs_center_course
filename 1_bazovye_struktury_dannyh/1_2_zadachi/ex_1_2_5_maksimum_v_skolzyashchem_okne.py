'''
Максимум в скользящем окне
Sample Input 1:

3
2 1 5
1
Sample Output 1:

2 1 5
Sample Input 2:

8
2 7 3 1 5 2 6 2
4
Sample Output 2:

7 7 5 6 6
'''


class StackMax:
    '''Описывает стек с хранением максимума.'''

    def __init__(self):
        self.array_val = []
        self.array_max_val = []

    def push(self, val):
        self.array_val.append(val)
        self._push_max(val)

    def _push_max(self, val):
        if self.array_max_val:
            new_val = max(self.array_max_val[-1], val)
        else:
            new_val = val
        self.array_max_val.append(new_val)

    def pop(self):
        if self.array_val:
            self.array_val.pop()
            self.array_max_val.pop()

    def max(self):
        return self.array_max_val[-1] if self.array_max_val else 0

    def last_val(self):
        return self.array_val[-1] if self.array_val else 0

    def __len__(self):
        return len(self.array_val)


class Queue:
    '''Описывает очередь с двумя стеками.'''

    def __init__(self, w_size):
        self.w_size = w_size
        self._put_lst = StackMax()
        self._get_lst = []
        self._max_lst = []

    def get_max_lst(self, array):
        '''Возвращает список максимумов.'''
        if self.w_size >= len(
                array):  # Если размер входного массива меньше размера окна, возвращаем максимум из ел.-ов массива:
            res = max(array)
            self._max_lst.append(res)
            return self._max_lst

        self._fill_left(array)  # Заполняем левый стек.

        while len(self._get_lst) + len(self._put_lst) == self.w_size:
            if not self._get_lst:  # Если правый стек пустой, заполняем максимумами правый стек и повторяем цикл.
                self._transfer_left_right()
                continue
            if not self._put_lst:  # Если левый пустой то берем максимум с правого.
                self._max_lst.append(self._get_lst.pop())
            else:  # Если левый и правый стеки не пусты, то сравниваем максимумы последних элементов, и ложем в результат. При этом последний элемент из правого удаляем.
                res = max(self._put_lst.max(), self._get_lst.pop())
                self._max_lst.append(res)
            if array:  # В левый стэк добавляем элемент из входного списка (если он есть).
                self._put_lst.push(array.pop(0))
        return self._max_lst

    def _fill_left(self, array):
        '''Заполняет левый стек элементами с входного массива.'''
        for i in range(self.w_size):
            self._put_lst.push(array.pop(0))

    def _transfer_left_right(self):
        '''Кладет максимумы последних элементов левого и правого стеков в правый стек, очищая от элементов левый стек'''
        for i in range(self.w_size):
            max_ = max(self._get_lst[-1],
                       self._put_lst.last_val()) if self._get_lst else self._put_lst.last_val()
            self._get_lst.append(max_)
            self._put_lst.pop()


# n = int(input())
# m = list(map(int, input().split()))
# w = int(input())
#
# q = Queue(w)
#
# print(*q.get_max_lst(m))

n = 7
m = [73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16]

q = Queue(n)
print(q.get_max_lst(m))