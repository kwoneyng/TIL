di = [(-1,0), (1,0), (0,-1), (0,1)]

for T in range(int(input())):
    n,m,k = map(int, input().split())
    bd = [[[] for i in range(n)] for i in range(n)]
    q = []
    merge = []
    rs_fin = 0
    for i in range(k):
        x, y, su, d = list(map(int, input().split()))
        d -= 1
        bd[x][y].append([su, d])
        q.append([x,y])
    for i in range(m):
        for i in range(len(q)):
            x,y = q.pop(0)
            su, d = bd[x][y].pop(0)
            dx, dy = di[d]
            X = x+dx
            Y = y+dy
            if 0 < X < n-1 and 0 < Y < n-1:
                if len(bd[X][Y]) == 0:
                    bd[X][Y].append([su, d])
                    if [X,Y] not in q:
                        q.append([X,Y])
                else:
                    bd[X][Y].append([su,d])
                    if [X,Y] not in merge:
                        merge.append([X,Y])
            elif X == 0 or X == n-1 or Y == 0 or Y == n-1:
                su //= 2
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
                bd[X][Y].append([su,d])
                if [X,Y] not in q:
                    q.append([X,Y])
        while merge:
            x,y = merge.pop(0)
            bd[x][y].sort(key=lambda x:x[0],reverse=True)
            rs, d = bd[x][y].pop(0)
            while bd[x][y]:
                rs += bd[x][y].pop()[0]
            bd[x][y].append([rs, d])
            if [x,y] not in q:
                q.append([x,y])
    while q:
        x,y = q.pop(0)
        rs_fin += bd[x][y][0][0]

    print('#{}'.format(T+1), rs_fin)