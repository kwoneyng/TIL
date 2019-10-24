near = [[-1,0],[0,1],[1,0],[0,-1]]

from collections import deque


def select(ox,oy,d1,d2,vis):
    x = ox
    y = oy
    rs =0
    vis[x][y] = 5
    rs += bd[x][y]
    vis[x-d1][y+d1] = 5
    rs += bd[x-d1][y+d1]
    vis[x+d2-d1][y+d2+d1] = 5
    rs += bd[x+d2-d1][y+d2+d1]
    vis[x+d2][y+d2] = 5
    rs += bd[x+d2][y+d2]
    dx,dy = -1,1
    while True:
        x += dx
        y += dy
        if vis[x][y] == 0:
            vis[x][y] = 5
            rs += bd[x][y]
        else:
            break
    dx,dy = 1,1
    while True:
        x += dx
        y += dy
        if vis[x][y] == 0:
            vis[x][y] = 5
            rs += bd[x][y]
        else:
            break
    dx,dy = 1, -1
    while True:
        x += dx
        y += dy
        if vis[x][y] == 0:
            vis[x][y] = 5
            rs += bd[x][y] 
        else:
            break
    dx,dy = -1,-1
    while True:
        x += dx
        y += dy
        if vis[x][y] == 0:
            vis[x][y] = 5
            rs += bd[x][y]
        else:
            break

    q = deque()
    q.append([x,y+d1])
    while q:
        x,y = q.popleft()
        vis[x][y] = 5
        rs += bd[x][y]
        for a,b in near:
            xi,yi = a+x,b+y
            if vis[xi][yi] == 0:
                q.append([xi,yi])
    dp[5] = rs
    rs = 0
    for i in range(ox):
        for j in range(oy+d1+1):
            if vis[i][j] == 0:
                # vis[i][j] = 1
                rs += bd[i][j]
    dp[1] = rs
    rs = 0
    for i in range(ox+1):
        for j in range(oy+d1+1,n):
            if vis[i][j] == 0:
                # vis[i][j] = 2
                rs += bd[i][j]
    dp[2] = rs
    rs = 0
    for i in range(ox,n):
        for j in range(oy+d1):
            if vis[i][j] == 0:
                # vis[i][j] = 3
                rs += bd[i][j]
    dp[3] = rs
    rs = 0
    for i in range(ox+1,n):
        for j in range(oy+d1,n):
            if vis[i][j] == 0:
                # vis[i][j] = 4
                rs += bd[i][j]
    dp[4] = rs
                
n=int(input())
bd = [list(map(int,input().split())) for i in range(n)]
ovis = [[0]*n for i in range(n)]
d_set = deque()

dp = [0]*6
mn = 999999999999999999999999999999999999

for d1 in range(1,n//2):
    for d2 in range(1,n//2):
        d_set.append([d1,d2])

# for d1,d2 in d_set:
#     for x in range(n):
#         for y in range(n):
#             print(x,y,d1,d2)
#             if 0 <= x - d1 + d2 0 <= x + d1 - d2 < n and x - d1 >= 0 and x + d2 < n and y+d1+d2 < n:
vis = [i[:] for i in ovis]
#                 select(x,y,d1,d2,vis)
#                 rs = max(dp)-min(dp)
#                 if mn > rs:
#                     mn = rs
# for i in vis:
#     print(i)
print(dp)
select(1,1,1,2,vis)
# select(3,1,1,1)
# print(dp)
