from collections import deque
direct = [[],[0,1],[0,-1],[-1,0],[1,0]]

def debug():
    for i in bdu:
        print(i)
    print('--------------')

def move(x,y,d):
    global stop
    temp = bdu[x][y][:]
    bdu[x][y] = []
    dx, dy = direct[d]
    xi,yi = x+dx,y+dy
    if 0 <= xi < n and 0 <= yi < n:
        if bdc[xi][yi] == 0:
            if not bdu[xi][yi]:
                q.append([xi,yi])
            bdu[xi][yi].extend(temp)
            if len(bdu[xi][yi]) >= 4:
                stop = 1
        elif bdc[xi][yi] == 1:
            if not bdu[xi][yi]:
                q.append([xi,yi])
            temp.reverse()
            bdu[xi][yi].extend(temp)
            if len(bdu[xi][yi]) >= 4:
                stop = 1
        elif bdc[xi][yi] == 2:
            if d == 1:
                temp[0] = 2
            elif d == 2:
                temp[0] = 1
            elif d == 3:
                temp[0] = 4
            elif d == 4:
                temp[0] = 3
            dx,dy = direct[temp[0]]
            xi,yi = x+dx, y+dy
            if 0 <= xi < n and 0 <= yi < n and bdc[xi][yi] != 2:
                if not bdu[xi][yi]:
                    q.append([xi,yi])
                bdu[xi][yi].extend(temp)
            else :
                bdu[x][y].extend(temp)
    else:
        if d == 1:
            temp[0] = 2
        elif d == 2:
            temp[0] = 1
        elif d == 3:
            temp[0] = 4
        elif d == 4:
            temp[0] = 3
        bdu[x][y].extend(temp)
        


n,k = map(int,input().split())
bdc = [list(map(int,input().split())) for i in range(n)]
bdu = [[[] for i in range(n)] for i in range(n)]
data = []
q = deque()
for i in range(k):
    x,y,d = list(map(int,input().split()))
    x -= 1
    y -= 1
    bdu[x][y].append(d)
    q.append([x,y])
stop = 0
debug()
for t in range(1,1001):
    for i in range(len(q)):
        x,y = q.popleft()
        d = bdu[x][y][0]
        move(x,y,d)
        debug()