bd = []
for i in range(4001):
    bd.append([0]*4001)
for T in range(int(input())):
    at = int(input())
    q = []
    rs = 0
    for i in range(at):
        y, x, di, k = list(map(int, input().split()))
        y = (y+1000)*2
        x = abs(x-1000)*2
        bd[x][y] = k
        dx, dy = (0,0)
        if di == 0:
            dx = -1
        elif di == 1:
            dx = 1
        elif di == 2:
            dy = -1
        elif di == 3:
            dy = 1
        q.append([x, y, dx, dy])
    while q:
        crush = []
        for i in range(len(q)):
            x,y,dx,dy = q.pop(0)
            if bd[x][y] == 0 :
                continue
            bd[x][y], temp = 0, bd[x][y]
            if 0 <= x+dx < 4001 and 0 <= y+dy < 4001:
                x += dx
                y += dy
                if bd[x][y] == 0:
                    bd[x][y] = temp
                    q.append([x,y,dx,dy])
                else :
                    bd[x][y] += temp
                    crush.append([x,y])
        for x, y in crush:
            rs += bd[x][y]
            bd[x][y] = 0
    print('#{}'.format(T+1),rs)