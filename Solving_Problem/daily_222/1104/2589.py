near = [(-1,0),(0,1),(1,0),(0,-1)]
from collections import deque

def go(x,y):
    global mx
    q = deque()
    vis=[[0]*c for i in range(r)]
    vis[x][y] = 1
    q.append([x,y,0])
    while q:
        for i in range(len(q)):
            x,y,cnt = q.popleft()
            for a,b in near:
                xi,yi = x+a, y+b
                if 0 <= xi < r and 0 <= yi < c:
                    if bd[xi][yi] == 'L' and vis[xi][yi] == 0:
                        vis[xi][yi] = 1
                        q.append([xi,yi,cnt+1])
    mx = max(mx, cnt)

r,c = map(int,input().split())
bd = [list(input()) for i in range(r)]
mx = 0
for x in range(r):
    for y in range(c):
        if bd[x][y] == 'L':
            go(x,y)
print(mx)