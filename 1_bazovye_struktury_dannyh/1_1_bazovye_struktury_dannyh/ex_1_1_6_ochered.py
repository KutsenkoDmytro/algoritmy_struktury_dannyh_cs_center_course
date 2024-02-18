#Реализация очереди с помощю двух стеков

class Queue:

    def __init__(self):
        self._put_lst = []
        self._get_lst = []

    def push_back(self, val):
        '''Кладет элемент в конец очереди.'''
        self._put_lst.append(val) # Кладем элемент в левый стек.

    def pop_front(self):
        '''Извлекает первый элемент очереди (и извлекает его).'''
        if self._get_lst: # Если правый стек не пустой, извлекаем последний элемент.
            return self._get_lst.pop()
        elif not self._put_lst: # Если левый стек пустой, то и очередь пустая.
            return False
        else: # Иначе перелаживаем элементы с левого в правый и извлекаем последний элемент.
            while self._put_lst:
                self._get_lst.insert(0,self._put_lst.pop(0))
            return self._get_lst.pop()


qu = Queue()
for i in range(5):
    qu.push_back(i)

print(qu.pop_front())
print(qu._get_lst) # 0
print(qu.pop_front()) # 1

