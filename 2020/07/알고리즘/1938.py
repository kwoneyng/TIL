from collections import deque
near4 = [[-1,0],[0,1],[1,0],[0,-1]]
near8 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def dfind(ht):
    x,y = ht[0]
    nx,ny = ht[1]
    if nx - x > 0:
        return 0  # 세로방향
    elif ny - y > 0:
        return 1  # 가로방향

def can_rotate(x,y):
    for a,b in near8:
        xi, yi = a+x, b+y
        if not 0 <= xi < n or not 0 <= yi < n or not bd[xi][yi] != '1':
            break
    else:
        return 1
    return 0


def moving():
    global rs
    vis = [[[0]*2 for i in range(n)] for i in range(n)]
    q = deque([bset])
    sx,sy,sd = bset
    vis[sx][sy][sd] = 1
    ex,ey,ed = eset
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            x,y,d = q.popleft()
            rd = (d+1)%2
            if can_rotate(x,y) and vis[x][y][rd]==0:
                q.append([x,y,rd])
                vis[x][y][rd] = 1
                
            for a,b in near4:
                xi,yi = a+x,b+y
                if xi == ex and yi == ey and ed == d:
                    rs = cnt
                    return
                if d == 0:
                    if 0 < xi < n-1 and 0 <= yi < n and bd[xi][yi] != '1' and bd[xi-1][yi] != '1' and bd[xi+1][yi] != '1' and vis[xi][yi][d] == 0:
                        q.append([xi,yi,d])
                        vis[xi][yi][d] = 1
                elif d == 1:
                    if 0 <= xi < n and 0 < yi < n-1 and bd[xi][yi] != '1' and bd[xi][yi-1] != '1' and bd[xi][yi+1] != '1' and vis[xi][yi][d] == 0:
                        q.append([xi,yi,d])
                        vis[xi][yi][d] = 1 
                
n = int(input())
bd = [list(input()) for i in range(n)]
bcnt = 0
ecnt = 0
rs = 0
bh = {}
eh = {}
for x in range(n):
    for y in range(n):
        if bd[x][y] == 'B':
            bh[bcnt] = x,y
            bcnt += 1
        elif bd[x][y] == 'E':
            eh[ecnt] = x,y
            ecnt += 1
bx, by = bh[1]
ex, ey = eh[1]
bset = [bx,by,dfind(bh)]
eset = [ex,ey,dfind(eh)]
moving()
print(rs)

