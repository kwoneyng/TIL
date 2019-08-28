def go():
    su = 0
    for i in bd:
        su += sum(i)
    if su > 50000:
        return 2
    rs = 0
    for x in range(n):
        for y in range(m):
            if bd[x][y] > 0 :
                rs += 1
                for a, b in near:
                    if 0 <= x+a < n and 0 <= y+b < m:
                        if bd[x+a][y+b] == 0:
                            melt[x][y] += 1
    if rs == 0 :
        return 2


def rs_ls(ls):
    for x in range(n):
        for y in range(m):
            ls[x][y] = 0
    return 0


def melting():
    for x in range(n):
        for y in range(m):
            if bd[x][y] - melt[x][y] > 0:
                bd[x][y] -= melt[x][y]
            else :
                bd[x][y] = 0
    return 0


def target(st_x, st_y):
    global is_cnt
    for x in range(st_x, n):
        for y in range(st_y, m):
            if vis[x][y] == 0:
                vis[x][y] = 1
                if bd[x][y] > 0 :
                    is_cnt += 1
                    start = [x, y+1]
                    que.append([x, y])
                    return 0


def finder():
    global is_cnt
    target(start[0], start[1])
    if is_cnt > 1:
        return 2
    while que:
        chk = que.pop(0)
        x, y = chk
        for a, b in near:
            if 0 <= x+a < n and 0 <= y+b < m:
                if vis[x+a][y+b] == 0:
                    vis[x+a][y+b] = 1
                    if bd[x+a][y+b] > 0:
                        que.append([x+a, y+b])
    rs = 0
    for i in vis:
        rs += i.count(0)
    if rs != 0 :
        return finder()


n, m = map(int, input().split())
near = [[-1, 0], [0, 1], [1, 0], [0, -1]]
bd = []
for i in range(n):
    bd.append(list(map(int, input().split())))
vis = []
for i in range(n):
    vis.append([0 for i in range(m)])
melt = []
for i in range(n):
    melt.append([0 for i in range(m)])
start = [0, 0]
que = []
cnt = 0

while True:
    cnt += 1
    is_cnt = 0
    if go() == 2:
        cnt = 0
        break
    melting()
    if finder() == 2:
        break
    rs_ls(melt)
    rs_ls(vis)
print(cnt)
