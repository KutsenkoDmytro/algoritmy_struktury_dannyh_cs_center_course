class Node:
    '''Описывает элемент двусвязного списка.'''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class TwoLinkedList:
    '''Описывает двусвязный список.'''

    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, obj):
        dupl = self.find_obj(obj.data)
        if dupl != None:  # не добавлять дубли.
            return

        ptr = self.head
        if ptr == None:
            self.tail = obj
        else:
            obj.next = ptr
            ptr.prev = obj
        self.head = obj

    def find_obj(self, data):
        ptr = self.head
        while ptr:
            if ptr.data == data:
                return ptr
            ptr = ptr.next
        return None

    def pop_front(self):
        if self.head == None:
            return
        ptr = self.head.next
        if ptr != None:
            ptr.prev = None
        else:
            self.tail = None
        self.head = ptr

    def pop_back(self):
        if self.tail == None:
            return
        ptr = self.tail.prev
        if ptr != None:
            ptr.next = None
        else:
            self.head = None
        self.tail = ptr

    def del_obj(self, data):
        obj = self.find_obj(data)
        if obj == None:  # если список пуст.
            return
        if obj.prev == None:  # если собираемся удалить первый элемент.
            self.pop_front()
            return
        if obj.next == None:  # если собираемся удалить последний элемент.
            self.pop_back()
            return

        left = obj.prev
        right = obj.next
        left.next = right
        right.prev = left

    def print_find_res(self, data):
        obj = self.find_obj(data)
        print('yes' if obj != None else 'no')

    def print_tl_list(self):
        ptr = self.head
        res = ''
        while ptr:
            res += f' {ptr.data}'
            ptr = ptr.next
        print(res.strip())


class Chain:
    '''Описывает объект для хеширования данных цепочками.'''
    P = 1000000007
    X = 263

    def __init__(self, length):
        self.m = length
        self.lst = [TwoLinkedList() for i in range(self.m + 1)]

    def hash_func(self, val: str):
        len_s = len(val)
        res = (sum([ord(val[i]) * (self.X ** i % self.P)
                    for i in range(len_s)]) % self.P) % self.m
        return res

    def add_(self, val: str):
        indx = self.hash_func(val)
        self.lst[indx].push_front(Node(val))

    def del_(self, val: str):
        indx = self.hash_func(val)
        self.lst[indx].del_obj(val)

    def find_(self, val: str):
        indx = self.hash_func(val)
        self.lst[indx].print_find_res(val)

    def check_(self, indx: int):
        self.lst[indx].print_tl_list()



n, m = [int(input()) for i in range(2)]
ch = Chain(n)

for i in range(m):
    cmd, val = input().split()
    if cmd == 'add':
        ch.add_(val)
    elif cmd == 'check':
        ch.check_(int(val))
    elif cmd == 'find':
        ch.find_(val)
    elif cmd == 'del':
        ch.del_(val)

# ch = Chain(5)
# ch.add_('world')
# ch.add_('HellO')
# ch.check_(4)
# ch.find_('World')
# ch.find_('world')
# ch.del_('world')
# ch.check_(4)
# ch.del_('HellO')
# ch.add_('luck')
# ch.add_('GooD')
# ch.check_(2)
# ch.del_('good')
