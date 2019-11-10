def catch():
    global rs
    target = 0
    depth = 200
    size = 0
    for i in range(m):
        if ht[i][1] == man:
            if depth > ht[i][0]:
                target = i
                size = ht[i][2]
                depth = ht[i][0]
            elif depth == ht[i][0]:
                if size < ht[i][2]:
                    target = i
                    size = ht[i][2]
    x,y,s,d,z = ht[target]
    if z > 0:
        rs += z
    bd[x][y] = 0
    ht[target] = [-1,-1,-1,-1,-1]
    
def move():
    vis = [[0]*c for i in range(r)]
    for i in range(m):
        if ht[i][0] > -1:
            x,y,s,d,z = ht[i]
            if d == 1:
                if x-s >= 0:
                    x = x-s
                elif -r < x - s < 0:
                    d = 2
                    x = abs(x-s)
                else :
                    x = abs(x-s+(r-1)*2)
            elif d == 2:
                if x+s < r:
                    x = x+s
                elif r <= x+s <= 2*(r-1):
                    d = 1
                    x = 2*(r-1) - (x+s)
                else :
                    x = x+s - 2*(r-1)
            elif d == 3:
                if y+s < c:
                    y = y+s
                elif c <= y+s <= 2*(c-1):
                    d = 4
                    y = 2*(c-1) - (y+s)
                else :
                    y = y+s - 2*(c-1)
            elif d == 4:
                if y-s >= 0:
                    y = y-s
                elif -c < y - s < 0:
                    d = 3
                    y = abs(y-s)
                else :
                    y = abs(y-s+(c-1)*2)
            if ht[vis[x][y]][4] < z:
                ht[vis[x][y]] = [-1,-1,-1,-1,-1]
                vis[x][y] = i
                ht[i] = [x,y,s,d,z]
            else :
                ht[i] = [-1,-1,-1,-1,-1]
    return vis


def debug():
    print(ht)
    for i in bd:
        print(i)


r,c,m = map(int,input().split())
bd = [[0]*c for i in range(r)]
ht = {}
rs = 0
for i in range(m):
    x,y,s,d,z = list(map(int,input().split()))
    x-=1
    y-=1
    if d < 3:
        s %= 2*(r-1)
    else :
        s %= 2*(c-1)
    ht[i] = [x,y,s,d,z]
    bd[x][y] = i
# debug()
if ht:
    for man in range(c):
        catch()
        bd = move()
        # debug()
print(rs)