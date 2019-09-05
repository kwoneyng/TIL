from pprint import pprint

def virus(ls):
    x, y = ls
    for dx, dy in near:
        X = x+dx
        Y = y+dy
        if 0 <= X < n and 0 <= Y < m:
            if n_bd[X][Y] == 0:
                n_bd[X][Y] = 2
                nls = [X, Y]
                virus(nls)


def mk_bd(ls, cnt= 0):
    n_bd = [i[:] for i in bd]
    for j in ls:
        x, y = j
        n_bd[x][y] = 1
    
    return n_bd


def bd_ck(ls):
    rs = 0
    for x in range(n):
        rs += ls[x].count(0)
    
    return rs

n, m = map(int,input().split())
bd = []
vi = []
can = []
c_set = []
rs_set = []
mx = 0
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(n):
    bd.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        if bd[x][y] == 2:
            vi.append([x,y])
        if bd[x][y] == 0:
            can.append([x,y])
lm = len(can)
for i in range(lm):
    for j in range(i+1, lm):
        for k in range(j+1, lm):
            c_set.append([can[i], can[j], can[k]])
for i in c_set:
    n_bd = mk_bd(i)
    for i in vi:
        virus(i)
    rs_set.append(bd_ck(n_bd))
print(max(rs_set))
