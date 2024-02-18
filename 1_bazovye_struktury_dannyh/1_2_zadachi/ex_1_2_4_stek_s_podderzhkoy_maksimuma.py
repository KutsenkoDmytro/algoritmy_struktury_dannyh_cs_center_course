'''
Стек с поддержкой максимума
Sample Input 1:

5
push 2
push 1
max
pop
max
Sample Output 1:

2
2
Sample Input 2:

5
push 1
push 2
max
pop
max
Sample Output 2:

2
1
Sample Input 3:

10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max
Sample Output 3:

9
9
9
9
'''

class Stack_max:

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
        print(self.array_max_val[-1] if self.array_max_val else 0)

# q = int(input())
# st = Stack_max()
# for i in range(q):
#     query = input()
#     if query == 'pop':
#         st.pop()
#     elif query == 'max':
#         st.max()
#     else:
#         st.push(int(query.split()[1]))

st = Stack_max()
st.push(2)
st.push(3)
st.push(9)
st.push(7)
st.push(2)
st.max()
st.max()
st.max()
st.pop()
st.max()

