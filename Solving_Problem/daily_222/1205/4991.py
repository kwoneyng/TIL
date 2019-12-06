from collections import deque
from heapq import heappop, heappush

near = [[-1,0], [0,1], [1,0], [0,-1]]

def val_cha(st,ed):
    temp = [i[:] for i in bd]
    sx,sy = ht[st]
    ex,ey = ht[ed]
    serve = deque()
    serve.append([sx,sy])
    cnt = 0
    while serve:
        cnt += 1
        for i in range(len(serve)):
            x,y = serve.popleft()
            if x == ex and y == ey:
                dt[st][ed] = cnt - 1
                dt[ed][st] = cnt - 1
                return 0
            for a,b in near:
                xi,yi = a+x, b+y
                if 0 <= xi < h and 0 <= yi < w and temp[xi][yi] != 'x':
                    temp[xi][yi] = 'x'
                    serve.append([xi, yi])
    return -1

                    
def build_root(vis, start=0, cnt=0):
    global rs
    if sum(vis) == dirty - 1:
        rs = min(rs, cnt)
        return 0
    for i in range(1,dirty):
        if not vis[i]:
            vis[i] = 1
            build_root(vis,i,cnt+dt[start][i])
            vis[i] = 0


while True:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    bd = [list(input()) for i in range(h)]

    dirty = 1
    rs = 9999999999999999999999
    ht = {}

    for x in range(h):
        for y in range(w):
            if bd[x][y] == 'o':
                ht[0] = [x,y]
            elif bd[x][y] == '*':
                ht[dirty] = [x,y]
                dirty += 1
    dt = {}
    for i in range(dirty):
        dt[i] = {}

    stop_flag = 0
    for i in range(dirty-1):
        if stop_flag == 0:
            for j in range(i+1,dirty):
                if val_cha(i,j) == -1:
                    print(-1)
                    stop_flag = 1
                    break
        else: 
            break

    if stop_flag == 0:
        vis = [0]*dirty
        build_root(vis)
        print(rs)

    
    
