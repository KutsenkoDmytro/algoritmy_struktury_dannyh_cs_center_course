'''
Поиск образца в тексте
Sample Input 1:

aba
abacaba
Sample Output 1:

0 4
Sample Input 2:

Test
testTesttesT
Sample Output 2:

4
Sample Input 3:

aaaaa
baaaaaaa
Sample Output 3:

1 2 3

'''



def my_hash(s:str):
    h = 0
    for char in s:
        h+= ord(char)
    return h

def my_rehash(h, new, old):
    h = h - ord(old) + ord(new)
    return h

def check(sub, s, start):
    return sub == s[start:(start+len(sub))]


def find_rabin_karp(s, sub):
    lst_res = []
    h_sub = my_hash(sub)
    l_sub = (len(sub))

    h = my_hash(s[0:l_sub])
    if h == h_sub:
        if check(sub, s, 0):
            lst_res.append(0)

    for pos in range(1,len(s)-l_sub + 1):
        h = my_rehash(h, s[pos + l_sub-1], s[pos-1])
        if h == h_sub:
            if check(sub, s, pos):
                lst_res.append(pos)

    return lst_res

sub, s = 'aba', 'abacaba' #[input() for i in range(2)]
print(*find_rabin_karp(s, sub))





