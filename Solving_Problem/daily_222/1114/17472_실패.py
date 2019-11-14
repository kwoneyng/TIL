from heapq import heappop, heappush

def numbering():
    cnt = 1
    for x in range(n):
        for y in range(m):
            if bd[x][y] == 1:
                if vis[x][y] == 0:
                    color(x,y,cnt)
                    cnt += 1
    return cnt


def color(x,y,cnt):
    vis[x][y] = cnt
    for a,b in near:
        xi, yi = a+x, b+y
        if 0 <= xi < n and 0 <= yi < m:
            if bd[xi][yi] == 1:
                if vis[xi][yi] == 0:
                    vis[xi][yi] = cnt
                    color(xi,yi,cnt)                


def distance():
    for x in range(n):
        start = 0
        end = 0
        length = 0
        for y in range(m):
            if not start:
                if vis[x][y] > 0:
                    start = vis[x][y]
            elif not end:
                if vis[x][y] == 0:
                    end = 1
                    length += 1
            elif end:
                if vis[x][y] == 0:
                    length += 1
                elif vis[x][y] > 0:
                    if length > 1:
                        dis[start][vis[x][y]] = length
                        dis[vis[x][y]][start] = length
                    start = vis[x][y]
                    end = 0
                    length = 0
    for y in range(m):
        start = 0
        end = 0
        length = 0
        for x in range(n):
            if not start:
                if vis[x][y] > 0:
                    start = vis[x][y]
            elif not end:
                if vis[x][y] == 0:
                    end = 1
                    length += 1
            elif end:
                if vis[x][y] == 0:
                    length += 1
                elif vis[x][y] > 0:
                    if length > 1:
                        dis[start][vis[x][y]] = length
                        dis[vis[x][y]][start] = length
                    start = vis[x][y]
                    end = 0
                    length = 0


def prim():
    q = [[0,1]]
    while q:
        cst, idx = heappop(q)
        connect[idx] = 1
        for i in range(1, cnt):
            if dis[idx][i] > 0 and connect[i] == 0 :
                cost[i] = min(dis[idx][i],cost[i])
                heappush(q, [cost[i], i])


near = [[-1,0],[0,1],[1,0],[0,-1]]
n, m = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]
vis = [[0]*m for i in range(n)]
cnt = numbering()
dis = [[0]*cnt for i in range(cnt)]
cost = [99999]*cnt
cost[0] = 0
cost[1] = 0
connect = [0]*cnt
connect[0] = 1
distance()
prim()
if sum(cost) > 100000:
    print(-1)
else:
    print(sum(cost))