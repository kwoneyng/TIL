from collections import deque

near = [[-1,0], [0,1], [1,0], [0,-1]]
def solve(bd,t):
    vis = [[1e9]*n for i in range(n)]
    q = deque([[0,0,0]]) # val, x, y
    vis[0][0] = 0
    while q:
        for i in range(len(q)):
            val, x, y = q.popleft()
            for a,b in near:
                xi, yi = a+x, b+y
                if 0 <= xi < n and 0 <= yi < n:
                    nval = val + bd[xi][yi]
                    if nval < vis[xi][yi]:
                        vis[xi][yi] = nval
                        q.append([nval, xi, yi])
    print(vis[n-1][n-1])
                    

for t in range(int(input())):
    n = int(input())
    bd = [list(map(int,input())) for i in range(n)]
    solve(bd,t)