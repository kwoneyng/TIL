for t in range(int(input())):
    n = int(input())
    m = int(input())
    bd = [[9999]*(n+1) for i in range(n+1)]
    for x in range(n+1):
        for y in range(n+1):
            if x == y:
                bd[x][y] = 0
    for i in range(m):
        a,b = map(int,input().split())
        bd[a][b] = 1
    for k in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if bd[x][y] > bd[x][k] + bd[k][y]:
                    bd[x][y] = bd[x][k] + bd[k][y]
    rs = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            if bd[x][y] >= 9999 and bd[y][x] >= 9999:
                break
        else:
            rs += 1
    print(f'#{t+1} {rs}')