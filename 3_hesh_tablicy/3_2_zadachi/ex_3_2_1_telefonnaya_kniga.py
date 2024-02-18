'''
Телефонная книга
Sample Input 1:

12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213
Sample Output 1:

Mom
not found
police
not found
Mom
daddy
Sample Input 2:

8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0
Sample Output 2:

not found
granny
me
not found
'''


class PhoneBook:
    '''Метод открытой адресации. Разрешение коллизий линейным исследованием.'''

    def __init__(self, n):
        self.size = n
        self.h_table = [None] * n

    def h_func(self, key, indx=0):
        return ((key % self.size) + indx) % self.size

    def _check_key_avail(self, key, indx):
        '''Проверяет принадлежность ключа, ячейке с указанным индексом.'''
        return type(self.h_table[indx]) is list and self.h_table[indx][0] == key


    def add_number_name(self, number, name):
        i = 0
        while i < self.size:
            indx = self.h_func(number, i)
            if self._check_key_avail(number, indx):
                self.h_table[indx][1] = name
                return
            elif self.h_table[indx] == None or self.h_table[indx] == 'del':
                self.h_table[indx] = [number,name]
                return
            i += 1

    def del_number(self, number):
        i = 0
        while i < self.size:
            indx = self.h_func(number, i)
            if self._check_key_avail(number, indx):
                self.h_table[indx] = 'del'
                return
            elif self.h_table[indx] == None:
                return
            i += 1

    def find_number(self, number):
        i = 0
        while i < self.size:
            indx = self.h_func(number, i)
            if self._check_key_avail(number, indx):
                return self.h_table[indx][1]
            elif self.h_table[indx] == None:
                break
            i += 1
        return 'not found'

n = int(input())

pb = PhoneBook(n)
for i in range(n):
    lst = input().split()
    if lst[0] == 'add':
        pb.add_number_name(int(lst[1]), lst[2])
    elif lst[0] == 'del':
        pb.del_number(int(lst[1]))
    else:
        print(pb.find_number(int(lst[1])))

# pb = PhoneBook(10)
# pb.add_number_name(76213,'Mom')
# pb.add_number_name(17239,'Bob')
# print(pb.find_number(17239))
# print(pb.find_number(76213))