near = [[-1,0],[0,1],[1,0],[0,-1]]

from collections import deque

def move(x,y,dx,dy):
    while bd[x][y] != '#' and bd[x][y] != 'O':
        x+=dx
        y+=dy
    return x-dx,y-dy
 

def bfs():
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt >= 10:
            break
        for dx,dy in near:
            nrx,nry=move(rx,ry,dx,dy)
            nbx,nby=move(bx,by,dx,dy)
        
            if bd[nbx][nby] == 'O':
                continue
            elif bd[nrx][nry] == 'O':
                print(cnt+1)
                return
    print(-1)



n,m = map(int, input().split())
bd=[list(input()) for i in range(n)]
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'R':
            rx,ry = x,y
        elif bd[x][y] == 'B':
            bx,by = x,y
q=deque()
q.append([rx,ry,bx,by,0])
