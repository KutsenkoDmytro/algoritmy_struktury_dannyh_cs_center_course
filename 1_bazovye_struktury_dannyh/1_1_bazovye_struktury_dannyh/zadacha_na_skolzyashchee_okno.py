'''
Задача:
Вход: последовательность чисел a1,a2,..an,
Выход: пройтись по последовательности окном размера m и вывести минимум в каждом из них.
Пример:

n = [5,1,3,2,4,6,1,7,3,2,8]
m = 3
'''

def get_min_list(n,m):
    ans = []

    if m >= len(n):
        ans.append(min(n))
    else:
        for i in range(0, len(n)-m+1):
            res = min(n[i:i+m])
            ans.append(res)
    return ans

n = [5,1,3,2,4,6,1,7,3,2,8]
m = 3

print(get_min_list(n,m))
