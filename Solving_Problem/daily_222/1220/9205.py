def go():
    q = [[0,st_x,st_y]]
    vis[0] = 1
    while q:
        idx, x, y = q.pop(0)
        if abs(x-ed_x) + abs(y-ed_y) <= 1000:
            print('happy')
            return
        for i, nx, ny in store:
            if vis[i] == 0:
                dt = abs(x-nx) + abs(y-ny)
                if dt <= 1000:
                    q.append([i,nx,ny])
                    vis[i] = 1
    print('sad')

for t in range(int(input())):
    n = int(input())
    st_x, st_y = map(int,input().split())
    vis = [0]*(n+1)
    store = []
    for i in range(1,n+1):
        x,y = map(int,input().split())
        store.append([i,x,y])
    ed_x, ed_y = map(int,input().split())
    go()