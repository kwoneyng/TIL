near = [[-1,0], [0,1], [1,0], [0,-1]]
from collections import deque

def finisher(p,st,ed):
    vis = [[[0]*4 for i in range(c)] for i in range(r)]
    sx, sy = node[st]
    ex, ey = node[ed]
    a,b = near[p]
    xi, yi = a+sx, b+sy
    q = deque()
    if 0 <= xi < r and 0 <= yi < c and bd[xi][yi] != '#':
        q.append([p,xi,yi])
        vis[xi][yi][p] = 1
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            d,x,y = q.popleft()
            if x == ex and y == ey:
                finded[st][ed][d] = cnt
                return
            for k in range(4):
                if d != k:
                    a,b = near[k]
                    xi, yi = x+a, b+y
                    if 0 <= xi < r and 0 <= yi < c and bd[xi][yi] != '#' and vis[xi][yi][k] == 0:
                        vis[xi][yi][k] = 1
                        q.append([k,xi,yi])

def starter(p,st,ed):
    vis = [[[0]*4 for i in range(c)] for i in range(r)]
    sx, sy = node[st]
    ex, ey = node[ed]
    a,b = near[p]
    xi, yi = a+sx, b+sy
    q = deque()
    if 0 <= xi < r and 0 <= yi < c and bd[xi][yi] != '#':
        q.append([p,xi,yi])
        vis[xi][yi][p] = 1
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            d,x,y = q.popleft()
            if x == ex and y == ey:
                finded[st][ed][p] = cnt
                return
            for k in range(4):
                if d != k:
                    a,b = near[k]
                    xi, yi = x+a, b+y
                    if 0 <= xi < r and 0 <= yi < c and bd[xi][yi] != '#' and vis[xi][yi][k] == 0:
                        vis[xi][yi][k] = 1
                        q.append([k,xi,yi])


r,c = map(int, input().split())
bd = [list(input()) for i in range(r)]

finded = [[[0]*4 for i in range(3)] for i in range(3)]
node = {}
gc = 1
for x in range(r):
    for y in range(c):
        if bd[x][y] == 'S':
            node[0] = x, y
        elif bd[x][y] == 'C':
            node[gc] = x,y
            gc += 1

for p in range(4):   # 방향관리 잘해야함
    finisher(p,0,1)
    finisher(p,0,2)
    starter(p,1,2)
    starter(p,2,1)

route = []

for p in range(4):
    if finded[0][1][p] > 0:
        for k in range(4):
            if p != k and finded[1][2][k] > 0:
                route.append(finded[0][1][p]+finded[1][2][k])

    if finded[0][2][p] > 0:
        for k in range(4):
            if p != k and finded[2][1][k] > 0:
                route.append(finded[0][2][p]+finded[2][1][k])

for i in finded:
    print(i)

if route:
    print(min(route))
else:
    print(-1)