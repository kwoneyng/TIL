# def move(ls):
#     global n
#     x, y = ls
#     u = bd[x][y].pop(0)
#     x, y, mi, f = u
#     if f == 1:
#         x -= 1
#         if x == 0:
#             mi = mi//2
#             f = 2
#     elif f == 2:
#         x += 1
#         if x == n-1:
#             mi = mi//2
#             f = 1
#     elif f == 3:
#         y -= 1
#         if y == 0:
#             mi = mi//2
#             f = 4
#     elif f == 4:
#         y += 1
#         if y == n-1:
#             mi = mi//2
#             f = 3
#     bd[x][y].append([x, y, mi, f])
#     if [x, y] not in fin_ls:
#         fin_ls.append([x, y])
#         q.append([x, y])
#     elif [x, y] not in col:
#         col.append([x, y])


# def merge(ls):
#     for i in range(len(ls)):
#         x, y = ls.pop(0)
#         rs = 0
#         bd[x][y].sort(key=lambda x:x[2], reverse=True)
#         for i in range(len(bd[x][y])-1):
#             a = bd[x][y].pop()
#             rs += a[2]
#         bd[x][y][0][2] += rs


# for T in range(int(input())):
#     n, m, k = list(map(int, input().split()))
#     bd = []
#     q = []
#     col = []
#     su = 0
#     for i in range(n):
#         bd.append([[] for i in range(n)])
#     for i in range(k):
#         s = list(map(int, input().split()))
#         q.append(s[:2])
#         bd[s[0]][s[1]].append(s)
#     while m > 0:
#         m -= 1
#         fin_ls = []
#         for i in range(len(q)):
#             a = q.pop(0)
#             move(a)
#         merge(col)
#     for i in q:
#         x, y = i
#         su += bd[x][y][0][2]
#     print('#{}'.format(T+1), su)
m = 5
m //= 3
print(m)