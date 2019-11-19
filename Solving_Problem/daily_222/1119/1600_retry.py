near = [[0,1],[1,0],[-1,0],[0,-1]]
horse = [[1,2],[2,1],[-2,1],[-1,2],[1,-2],[2,-1],[-1,-2],[-2,-1]]
from collections import deque

def go(x=0, y=0, cnt=0, hs=0):
    global mn
    q = deque()
    q.append([x,y,cnt,hs])
    while q:
        for i in range(len(q)):
            x,y,cnt,hs = q.popleft()
            if x == h-1 and y == w-1:
                mn = min(mn,cnt)
                return
            elif cnt < mn:
                if hs < k:
                    for a,b in horse:
                        xi, yi = a+x, b+y
                        if 0 <= xi < h and 0 <= yi < w and bd[xi][yi] == 0 and vis[hs+1][xi][yi] == 0:
                            vis[hs+1][xi][yi] = 1
                            q.append([xi,yi,cnt+1,hs+1])
                for a,b in near:
                    xi, yi = a+x, b+y
                    if 0 <= xi < h and 0 <= yi < w and bd[xi][yi] == 0 and vis[hs][xi][yi] == 0:
                        vis[hs][xi][yi] = 1
                        q.append([xi,yi,cnt+1,hs])


k = int(input())
w,h = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(h)]
vis = [[[0]*200 for i in range(200)] for i in range(31)]
mn = 99999999999999999
go()
if mn >= 999999999999999:
    print(-1)
else:
    print(mn)