'''
Симуляция обработки сетевых пакетов
Sample Input 1:

1 0
Sample Output 1:

Sample Input 2:

1 1
0 0
Sample Output 2:

0
Sample Input 3:

1 1
0 1
Sample Output 3:

0

'''


class Package:

    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration
        self.start_t = -1
        self.end_t = -1

class Processor:

    def __init__(self, buf_size):
        self.buf_size = buf_size
        self.buffer = []
        self.ptr = 0 #Стартовое время для поступившего пакета.

    def process_package(self, package):
        '''Метод обработки пакета.'''
        if self.buffer_not_filled():
            self.push_buffer(package)
        else:
            while self.buffer and self.buffer[0].end_t <= package.arrival:
                self.buffer.pop(0)
            if self.buffer_not_filled():
                self.push_buffer(package)

    def push_buffer(self, package):
        '''Помещает пакет в буффер.'''
        package.start_t = max(self.ptr, package.arrival)
        package.end_t = self.ptr = package.start_t + package.duration
        self.buffer.append(package)

    def buffer_not_filled(self):
        '''Проверяет буффер на заполненность.'''
        return self.buf_size > len(self.buffer)


# size, n = map(int, input().split())
# packeges = [Package(*map(int, input().split())) for i in range(n)]
# pr = Processor(size)
# for p in packeges:
#     pr.process_package(p)
#     print(p.start_t)


lst = [
       (16, 0),
       (29, 3),
       (44, 6),
       (58, 0),
       (72, 2),
       (88, 8),
       (95, 7),
       (108, 6),
       (123, 9),
       (139, 6),
       (152, 6),
       (157, 3),
       (169, 3),
       (183, 1),
       (192, 0),
       (202, 8),
       (213, 8),
       (229, 3),
       (232, 3),
       (236, 3),
       (239, 4),
       (247, 8),
       (251, 2),
       (267, 7),
       (275, 7)]

packeges = [Package(*i) for i in lst]
pr = Processor(1)
for p in packeges:
    pr.process_package(p)
    print(p.start_t)
