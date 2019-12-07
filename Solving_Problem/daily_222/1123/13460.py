from collections import deque
near = [[-1,0],[0,1],[1,0],[0,-1]]

def rolling(rx,ry,bx,by,d):
    dx,dy = near[d]
    stop = [0,0]
    hole = [0,0]
    dt = [0,0]
    while sum(stop) < 2:
        if stop[0] == 0:
            rx += dx
            ry += dy
            dt[0] += 1
            if bd[rx][ry] == '#':
                rx -= dx
                ry -= dy
                stop[0] = 1
            elif bd[rx][ry] == 'O':
                stop[0] = 1
                hole[0] = 1
        if stop[1] == 0:
            bx += dx
            by += dy
            dt[1] += 1
            if bd[bx][by] == '#':
                bx -= dx
                by -= dy
                stop[1] = 1
            elif bd[bx][by] == 'O':
                stop[1] = 1
                hole[1] = 1
    if rx == bx and ry == by:
        if dt[0] < dt[1]:
            bx -= dx
            by -= dy
        else :
            rx -= dx
            ry -= dy

    return rx,ry,bx,by,hole[0],hole[1]


def start():
    global rs
    q = deque()
    q.append(ht['R']+ht['B'])
    cnt = 0
    while q:
        cnt += 1
        if cnt > 10:
            return
        for i in range(len(q)):
            rx,ry,bx,by = q.popleft()
            for d in range(4):
                rnx,rny,bnx,bny,success,fail = rolling(rx,ry,bx,by,d)
                if fail == 1:
                    pass
                elif success == 1:
                    rs = cnt
                    return
                elif vis[rnx][rny][bnx][bny] == 0:
                    q.append([rnx,rny,bnx,bny])
                    vis[rnx][rny][bnx][bny] = 1


n,m = map(int,input().split())
bd = [list(input()) for i in range(n)]
vis = [[[[0]*m for i in range(n)]for i in range(11)]for i in range(11)]
ht = {}
rs = -1
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'B':
            ht['B'] = [x,y]
        elif bd[x][y] == 'R':
            ht['R'] = [x,y]
        elif bd[x][y] == 'O':
            ht['O'] = [x,y]
start()
print(rs)