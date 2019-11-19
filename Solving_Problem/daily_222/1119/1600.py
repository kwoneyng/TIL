from collections import deque
near = [[0,1],[1,0],[-1,0],[0,-1]]
horse = [[1,2],[2,1],[-2,1],[-1,2],[1,-2],[2,-1],[-1,-2],[-2,-1]]

def go(x=0,y=0,cnt=0,ho=0):
    global mn
    if mn < cnt:
        return
    elif x == h-1 and y == w-1:
        mn = min(mn, cnt)
        return
    if ho < k:
        for a,b in horse:
            xi, yi = a+x, b+y
            if 0 <= xi < h and 0 <= yi < w and bd[xi][yi] == 0 and vis[xi][yi] == 0:
                vis[xi][yi] = 1
                go(xi,yi,cnt+1,ho+1)
                vis[xi][yi] = 0
    for a,b in near:
        xi, yi = a+x, b+y
        if 0 <= xi < h and 0 <= yi < w and bd[xi][yi] == 0 and vis[xi][yi] == 0:
            vis[xi][yi] = 1
            go(xi,yi,cnt+1,ho)
            vis[xi][yi] = 0


k = int(input())
w, h = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(h)]
vis = [[0]*w for i in range(h)]
mn = 99999999999
go()
print(mn)