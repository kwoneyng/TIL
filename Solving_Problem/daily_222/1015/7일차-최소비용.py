from heapq import heappush, heappop
near = [(-1,0),(0,-1),(1,0),(0,1)]
for t in range(int(input())):
    n = int(input())
    bd = [list(map(int,input().split())) for i in range(n)]
    dp = [[9999999999999]*(n) for i in range(n)]
    dp[0][0] = 0
    q = []
    heappush(q,[0,0,0])
    while q:
        val,x,y = heappop(q)
        for a,b in near:
            xi,yi = x+a,y+b
            if 0 <= xi < n and 0 <= yi < n:
                dt = 1
                if bd[xi][yi] > bd[x][y]:
                    dt += bd[xi][yi] - bd[x][y]
                dval = val + dt
                if dp[xi][yi] > dval:
                    dp[xi][yi] = dval
                    heappush(q,[dval,xi,yi])
    print('#{}'.format(t+1),dp[-1][-1])