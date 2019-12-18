import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    t = list(map(int,input().split()))
    bd = [[0]*(n+1) for i in range(n+1)]
    for i in range(n-1):
        for j in range(i+1,n):
            bd[t[i]][t[j]] = -1
            bd[t[j]][t[i]] = 1

    for i in range(int(input())):
        a,b = list(map(int, input().split()))
        bd[a][b] = -bd[a][b]
        bd[b][a] = -bd[b][a]
    stop = 0
    rs = [-1]*n
    for x in range(1,n+1):
        seat = 0
        odd = 0
        for y in range(1,n+1):
            if bd[x][y] == 1:
                seat += 1
            elif bd[x][y] == 0:
                odd += 1
        if odd > 1:
            print('?',end='')
            stop = 1
            break
        else:
            rs[seat] = x
    if rs.count(-1):
        if stop == 0:
            print('IMPOSSIBLE',end='')
    else:
        for i in rs:
            print(i,end=' ')
    print()