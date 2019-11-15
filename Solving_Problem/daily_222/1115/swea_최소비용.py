from collections import deque
from heapq import heappop, heappush
near = [[-1,0],[0,1],[1,0],[0,-1]]

for t in range(1,int(input())+1):
    n = int(input())
    bd = [list(map(int,input().split())) for i in range(n)]
    dp = [[99999]*n for i in range(n)]
    dp[0][0] = 0
    q = []
    heappush(q,[0,0,0])
    while q:
        rs, x, y = heappop(q)
        for a,b in near:
            xi,yi = a+x,b+y
            if 0 <= xi < n and 0 <= yi < n:
                add = 0
                if bd[xi][yi] - bd[x][y] > 0:
                    add = bd[xi][yi] - bd[x][y]
                cnt = 1 + add + rs
                if cnt < dp[xi][yi]:
                    dp[xi][yi] = cnt
                    heappush(q,[cnt,xi,yi])
    print(f'#{t} {dp[-1][-1]}')