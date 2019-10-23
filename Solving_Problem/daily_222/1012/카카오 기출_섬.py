# 섬 번호
# 바깥쪽 부터 안전한 섬 찾기
# 찾았을 때 전체 섬 갱신
near = [[-1,0],[0,1],[1,0],[0,-1]]

def numbering(x,y):
    global cnt
    q = [(x,y)]
    if bd[x][y] == '#':
        bd[x][y] = cnt
        vis[x][y] = 1
    else :
        vis[x][y] = 1
        return 0
    while q:
        x,y = q.pop()
        for a,b in near:
            xi, yi = a+x, b+y
            if 0 <= xi < n and 0 <= yi < m:
                if vis[xi][yi] == 0 :
                    if bd[xi][yi] == '#':
                        vis[xi][yi] = 1
                        bd[xi][yi] = cnt
                        q.append((xi,yi))

def go(ls):
    q = [ls]
    while q:
        x,y,cv = q.pop()
        nvis[x][y] = 0
        for a,b in near:
            xi, yi = x+a, y+b
            if 0<=xi<n and 0<=yi<m:
                nv = bd[xi][yi]
                if nvis[xi][yi] == 1:
                    nvis[xi][yi] = 0
                    if nv == '.' or nv == cv:
                        q.append((xi,yi,cv))
                    else :
                        if nv not in nxt_ls[cv]:
                            nxt_ls[cv].append(nv)
                            start.append([xi,yi,nv])
                        if cv not in nxt_ls[nv]:
                            nxt_ls[nv].append(cv)
                    



n,m = map(int, input().split())
bd = [list(input()) for i in range(n)]
cnt = 1
vis = [[0]*m for i in range(n)]
for x in range(n):
    for y in range(m):
        if numbering(x,y) != 0:
            cnt += 1
start = [(0,0,0)]
nxt_ls = [[] for i in range(cnt)]
while True:
    for i in range(len(start)):
        nvis = [i[:] for i in vis]
        ls = start.pop(0)
        go(ls)
    vis = nvis

for i in bd:
    print(i)
for i in vis:
    print(i)
print(nxt_ls)
print(start)