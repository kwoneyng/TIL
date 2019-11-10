from collections import deque
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def go():
    x,y,size,eat = q.popleft()
    vis = [[0]*n for i in range(n)]
    vis[x][y] = 1
    for j in range(4):
        a,b = dx[j],dy[j]
        xi, yi = a+x, b+y
        if 0 <= xi < n and 0 <= yi < n and vis[xi][yi] == 0:
            if size > bd[xi][yi]:
                if bd[xi][yi] == 0:
                    q.append([x,y,size,eat])


n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
shark={}
q = deque()
for x in range(n):
    for y in range(n):
        if bd[x][y] == 9:
            q.append([x,y,size,eat])
            st_x, st_y = x,y
for time in range(10000):
    for i in range(len(q)):
        go()