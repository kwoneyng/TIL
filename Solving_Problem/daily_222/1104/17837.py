def debug():
    print(f'ht =',ht)
    for i in bd:
        print(i)
    print('----------')

def move():
    for i in range(k):
        x,y,d = ht[i]
        idx = bd[x][y].index(i)
        temp = bd[x][y][idx:]
        del bd[x][y][idx:]
        if d == 1:
            a,b = 0,1
        elif d == 2:
            a,b = 0,-1
        elif d == 3:
            a,b = -1,0
        elif d == 4:
            a,b = 1,0
        xi,yi = x+a, y+b
        if 0 <= xi < n and 0 <= yi < n:
            if color[xi][yi] == 0:
                white(xi,yi,temp)
            elif color[xi][yi] == 1:
                red(xi,yi,temp)
            elif color[xi][yi] == 2:
                blue(x,y,d,temp)
        else:
            blue(x,y,d,temp)


def white(x,y,temp):
    global stop
    for i in temp:
        d = ht[i][2]
        ht[i] = [x,y,d]
        bd[x][y].append(i)
    if len(bd[x][y]) >= 4:
        stop = 1


def red(x,y,temp):
    global stop
    temp.reverse()
    for i in temp:
        d = ht[i][2]
        ht[i] = [x,y,d]
        bd[x][y].append(i)
    if len(bd[x][y]) >= 4:
        stop = 1

def blue(x,y,d,temp):
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    elif d == 4:
        d = 3
    if d == 1:
        a,b = 0,1
    elif d == 2:
        a,b = 0,-1
    elif d == 3:
        a,b = -1,0
    elif d == 4:
        a,b = 1,0
    ht[temp[0]][2] = d
    xi,yi = x+a, y+b
    if 0 <= xi < n and 0 <= yi < n:
        if color[xi][yi] == 0:
            white(xi,yi,temp)
        elif color[xi][yi] == 1:
            red(xi,yi,temp)
        elif color[xi][yi] == 2:
            white(x,y,temp)
    else:
        white(x,y,temp)
    


ht = {}
n, k = map(int, input().split())
color=[list(map(int,input().split())) for i in range(n)]
bd=[[[] for i in range(n)] for i in range(n)]
q=[]
for i in range(k):
    x,y,d = list(map(int,input().split()))
    x-=1
    y-=1
    bd[x][y].append(i)
    ht[i] = [x,y,d]
stop = 0
for i in range(1,1001):
    move()
    if stop == 1:
        print(i)
        break
else:
    print(-1)