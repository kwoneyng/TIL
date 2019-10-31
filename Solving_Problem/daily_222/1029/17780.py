di = [[],[0,1],[0,-1],[-1,0],[1,0]]
def move(j):
    x,y = ht[j]
    if x < 0 :
        return
    else:
        idx, d = bd[x][y][0]
        temp = bd[x][y][:]
        bd[x][y] = []
        dx,dy = di[d]
        xi,yi = x+dx, y+dy
        if 0 <= xi < n and 0 <= yi < n:
            if color[xi][yi] == 0:
                white(xi,yi,temp)
            elif color[xi][yi] == 1:
                ht[idx] = [-1,-1]
                red(xi,yi,temp)
            elif color[xi][yi] == 2:
                blue(x,y,d,temp)
        else:
            blue(x,y,d,temp)

def white(x,y,temp):
    idx = temp[0][0]
    if bd[x][y]:
        ht[idx] = [-1,-1]
    else:
        ht[idx] = [x,y]
    bd[x][y].extend(temp)


def red(x,y,temp):
    temp.reverse()
    idx = temp[0][0]
    if not bd[x][y]:
        ht[idx] = [x, y]
    bd[x][y].extend(temp)

def blue(x,y,d,temp):
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    elif d == 4:
        d = 3
    temp[0][1] = d
    idx = temp[0][0]
    dx, dy = di[d]
    xi, yi = x+dx, y+dy
    if 0 <= xi < n and 0 <= yi < n:
        if color[xi][yi] == 0:
            white(xi,yi,temp)
        elif color[xi][yi] == 1:
            ht[idx]=[-1,-1]
            red(xi,yi,temp)
        else:
            white(x,y,temp)
    else:
        white(x,y,temp)

def debug():
    print('--------')
    print(f'j = {j}')
    print(ht)
    for i in bd:
        print(i)

def stop():
    for i in range(k):
        x,y = ht[i]
        if bd[x][y]:
            if len(bd[x][y]) >= 4:
                return 1



n,k = map(int,input().split())
color = [list(map(int,input().split())) for i in range(n)]
bd = [[[] for i in range(n)] for i in range(n)]
ht = {}
for i in range(k):
    x,y,d = list(map(int,input().split()))
    x-=1
    y-=1
    bd[x][y].append([i,d])
    ht[i] = [x,y]

for i in range(1,1001):
    for j in range(k):
        move(j)
    if stop() == 1:
        print(i)
        break
else:
    print(-1)


