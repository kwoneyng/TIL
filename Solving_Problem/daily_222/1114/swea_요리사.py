from collections import deque

def perm(vis, s=0):
    global mn
    if sum(vis) == n/2:
        rs1 = 0
        rs2 = 0
        for x in range(n-1):
            for y in range(x,n):
                if vis[x] == vis[y] and vis[x] == 0:
                    rs1 += bd[x][y]
                    rs1 += bd[y][x]
                elif vis[x] == vis[y]:
                    rs2 += bd[x][y]
                    rs2 += bd[y][x]
        rs = abs(rs1-rs2)
        mn = min(rs, mn)
        return
    for i in range(s,n):
        vis[i] = 1
        perm(vis, i+1)
        vis[i] = 0


for t in range(int(input())):
    n = int(input())
    bd = [list(map(int,input().split())) for i in range(n)]
    mn = 9999999999999999999999999
    vis=[0]*n
    perm(vis)
    print(f'#{t+1} {mn}')