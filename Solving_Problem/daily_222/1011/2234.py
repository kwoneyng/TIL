near = [[0,1],[1,0],[0,-1],[-1,0]]

def perm(y,x=1,ls=[]):
    if len(ls) == 2:
        perm_set.append(ls)
    for i in range(x,y):
        perm(y,i+1,ls+[i])

def go(x,y):
    global cnt, p, full
    if vis[x][y] == 0:
        vis[x][y] = cnt
        p += 1
        full -= 1
        for i in range(4):
            a,b = near[i]
            xi, yi = (x+a, y+b)
            if 0 <= xi < m and 0 <= yi < n:
                if not bd[xi][yi] & (1<<i):
                    go(xi,yi)
                else:
                    if [xi,yi] not in wall:
                        wall.append([xi,yi])

n,m = map(int, input().split())
bd = [list(map(int, input().split())) for i in range(m)]
vis = [[0]*n for i in range(m)]
su = []
wall = []
cnt = 1
full = n*m
perm_set =[]
for x in range(m):
    if full == 0:
        break
    for y in range(n):
        if full == 0:
            break
        if vis[x][y] == 0:
            p = 0
            go(x,y)
            su.append(p)
            cnt += 1
print(cnt-1)
print(max(su))
mx = 0
for x,y in wall:
    for a,b in near:
        xi, yi = x+a, y+b
        if 0 <= xi < m and 0 <= yi < n:
            if vis[x][y] != vis[xi][yi]:
                if [vis[x][y], vis[xi][yi]] not in perm_set:
                    perm_set.append([vis[x][y],vis[xi][yi]])
for x,y in perm_set:
    a = su[x-1]+su[y-1]
    if mx < a:
        mx = a
print(mx)
