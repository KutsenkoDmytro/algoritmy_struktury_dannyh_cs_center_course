'''
Расстановка скобок в коде
Sample Input 1:

([](){([])})
Sample Output 1:

Success
Sample Input 2:

()[]}
Sample Output 2:

5
Sample Input 3:

{{[()]]
Sample Output 3:

7
'''

def check_brackets(st):
    opening_br = ['(','{','[',]
    closing_br = {']':'[', '}':'{', ')':'('}

    lst = [] # Массив для хранения элементов без пар в формате кортежей (ел., индекс).
    for k, v in enumerate(st):
        if v in opening_br:
            lst.append((v,k))
        elif not lst and v in closing_br:
            return k + 1
        elif v in closing_br:
            if lst[-1][0] != closing_br[v]:
                return k + 1  # Возвращаем индекс ошибочной закрывающей скобки + 1.
            lst.pop()
    return lst[0][1] + 1 if lst else 'Success' # Возвращаем индекс ошибочной открывающей скобки + 1 или успех.


#print(check_brackets(input()))

st = '([](){([])})'
print(check_brackets(st))