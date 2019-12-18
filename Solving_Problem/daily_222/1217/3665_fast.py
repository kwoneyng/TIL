import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    t = list(map(int,input().split()))
    bd = [[0]*(n+1) for i in range(n+1)]
    deseat = [0]*(n+1)
    zrcnt = n*n-n
    for i in range(n-1):
        for j in range(i+1,n):
            bd[t[i]][t[j]] = -1
            bd[t[j]][t[i]] = 1
            deseat[t[j]] += 1
            zrcnt -= 2
    
    for i in range(int(input())):
        a,b = list(map(int,input().split()))
        if bd[a][b] == 1:
            deseat[a] -= 1
            deseat[b] += 1
        else:
            deseat[a] += 1
            deseat[b] -= 1
    
    if zrcnt > 0:
        print('?')
    elif sorted(deseat[1:]) != [i for i in range(n)]:
        print('IMPOSSIBLE')
    else:
        rs = [0]*n
        for i in range(1,n+1):
            rs[deseat[i]] = str(i)
        print(' '.join(rs))
