# a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# d = list(enumerate(a))
# for T in range(int(input())):
#     st_i, t_c = list(input().split())
#     print(st_i)
#     s = input().split()
#     for i in range(len(s)):
#         for z in d:
#             if s[i] in z:
#                 s[i] = z[0]
#                 break
#     s.sort()
#     for j in range(len(s)):
#         for k in d:
#             if s[j] in k:
#                 print(k[1], end=' ')
#     print('')                

# a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# d = [(0, 'ZRO'), (1, 'ONE'), (2, 'TWO'), (3, 'THR'), (4, 'FOR'), (5, 'FIV'), (6, 'SIX'), (7, 'SVN'), (8, 'EGT'), (9, 'NIN')]
# for T in range(int(input())):
#     st_i, t_c = list(input().split())
#     print(st_i)
#     s = input().split()
#     for i in range(len(s)):
#         for z in d:
#             if s[i] in z:
#                 s[i] = z[0]
#                 break
#     s.sort()
#     for j in range(len(s)):
#         for k in d:
#             if s[j] in k:
#                 print(k[1], end=' ')
#     print('')                

def Q_sort(ls):
    sl = []
    bl = []
    el = []
    if len(ls) <= 1:
        return ls
    else:
        start = int(ls[0])
        while len(ls) > 0:
            nxt = int(ls.pop())
            if nxt > start:
                bl.append(nxt)
            elif nxt < start:
                sl.append(nxt)
            else :
                el.append(nxt)
        return Q_sort(sl) + el + Q_sort(bl)


su_set = {
    'ZRO' : '0',
    'ONE' : '1',
    'TWO' : '2',
    'THR' : '3',
    'FOR' : '4',
    'FIV' : '5',
    'SIX' : '6',
    'SVN' : '7',
    'EGT' : '8',
    'NIN' : '9',
}

st_set = {
    0 : 'ZRO',
    1 : 'ONE',
    2 : 'TWO',
    3 : 'THR',
    4 : 'FOR',
    5 : 'FIV',
    6 : 'SIX',
    7 : 'SVN',
    8 : 'EGT',
    9 : 'NIN',
}

for T in range(int(input())):
    s, su = input().split()
    su = int(su)
    N = list(map(str, input().split()))
    N_r = ['0']*len(N)
    for i in range(len(N)):
        N_r[i] = su_set[N[i]]
    N_rs = Q_sort(N_r)
    for j in range(len(N_rs)):
        N_r.append(st_set[N_rs[j]])
    print(s)
    for i in N_r:
        print(i,end=' ')
    