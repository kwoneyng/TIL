from collections import deque
near = [[-1,0],[0,1],[1,0],[0,-1]]

def go():
    q = deque([[0,0,sx,sy]])
    vis = [[[9999,9999] for i in range(m)] for i in range(n)]
    while q:
        cg,cn,x,y = q.popleft()
        for a,b in near:
            xi, yi = x+a, y+b
            if 0 <= xi < n and 0 <= yi < m:
                if bd[xi][yi] == 'g':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg+1, cn, xi, yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg+1, cn, xi, yi])
                elif bd[xi][yi] == 'n':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg, cn+1, xi, yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg, cn+1, xi, yi])
                elif bd[xi][yi] == '.':
                    if vis[xi][yi][0] > cg:
                        vis[xi][yi] = [cg,cn]
                        q.append([cg,cn,xi,yi])
                    elif vis[xi][yi][0] == cg:
                        if vis[xi][yi][1] > cn:
                            vis[xi][yi] = [cg,cn]
                            q.append([cg,cn,xi,yi])
    return vis[fx][fy]

n,m = map(int,input().split())
bd = [list(input()) for i in range(n)]
gbg = []
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'S':
            sx,sy = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'F':
            fx,fy = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'g':
            gbg.append([x,y])

for x,y in gbg:
    for a,b in near:
        xi, yi = x+a, y+b
        if 0 <= xi < n and 0 <= yi < m:
            if bd[xi][yi] == '.':
                bd[xi][yi] = 'n'

for i in go():
    print(i,end=' ')