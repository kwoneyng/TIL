from collections import deque

near = [[-1,0], [0,1], [1,0], [0,-1]]

def give():
    global rs
    vis = [[[[[0]*2 for i in range(2)] for i in range(4)] for i in range(m)] for i in range(n)]
    x,y = ht[0]
    gx1,gy1 = ht[1]
    gx2,gy2 = ht[2]
    q = deque([[x,y,5,0,0]])
    time = 0
    while q:
        time += 1
        for _ in range(len(q)):
            x,y,d,g1,g2 = q.popleft()
            ng1 = g1
            ng2 = g2
            for i in range(4):
                if d != i:
                    a,b = near[i]
                    xi,yi = a+x,b+y
                    if 0 <= xi < n and 0 <= yi < m and bd[xi][yi] != '#' and vis[xi][yi][i][g1][g2] == 0:
                        vis[xi][yi][i][g1][g2] = 1
                        if g1 == 0 and xi == gx1 and yi == gy1:
                            if g2 == 1:
                                rs = time
                                return
                            ng1 = 1
                        elif g2 == 0 and xi == gx2 and yi == gy2:
                            if g1 == 1:
                                rs = time
                                return
                            ng2 = 1
                        q.append([xi,yi,i,ng1,ng2])


n, m = map(int,input().split())
bd = [list(input()) for i in range(n)]
ht = {}
gft = 1
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'S':
            ht[0] = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'C':
            ht[gft] = [x,y]
            bd[x][y] = '.'
            gft += 1
rs = -1
give()
print(rs)