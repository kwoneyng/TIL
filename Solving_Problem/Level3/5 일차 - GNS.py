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

a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
d = [(0, 'ZRO'), (1, 'ONE'), (2, 'TWO'), (3, 'THR'), (4, 'FOR'), (5, 'FIV'), (6, 'SIX'), (7, 'SVN'), (8, 'EGT'), (9, 'NIN')]
for T in range(int(input())):
    st_i, t_c = list(input().split())
    print(st_i)
    s = input().split()
    for i in range(len(s)):
        for z in d:
            if s[i] in z:
                s[i] = z[0]
                break
    s.sort()
    for j in range(len(s)):
        for k in d:
            if s[j] in k:
                print(k[1], end=' ')
    print('')                
