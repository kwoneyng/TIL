from pprint import pprint

def ch_chic(idx, ls):
    global m
    if len(ls) == m:
        if ls not in ch_ch:
            ch_ch.append(ls)
        return 0
    for j in range(idx+1, len(chic)):
        ch_chic(j, ls+[chic[j]])


n, m = map(int, input().split())
bd = [list(map(int, input().split())) for i in range(n)]
chic = []
home = []
ch_ch = []
for x in range(n):
    for y in range(n):
        if bd[x][y] == 2:
            chic.append([x, y])
        elif bd[x][y] == 1:
            home.append([x, y])

for i in range(len(chic)):
    ch_chic(i,[chic[i]])
mn_rs = 1000000
for i in ch_ch:
    rs = 0
    for j in home:
        su = 1000
        for k in i:
            hx, hy = j
            cx, cy = k
            a = abs(hx-cx) + abs(hy-cy)
            if su > a :
                su = a
        rs += su
        if rs > mn_rs:
            break
    if mn_rs > rs:
        mn_rs = rs

print(mn_rs)