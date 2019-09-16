def find(flr=0, rs=1):
    global mx, n
    if flr == n :
        if rs > mx:
            mx = rs
            return 0
    if rs <= mx:
        return 0
    for i in range(n):
        if not vis[i]:
            vis[i] = 1
            find(flr+1, rs*bd[flr][i])
            vis[i] = 0

for T in range(int(input())):
    n = int(input())
    bd = [list(map(int, input().split())) for i in range(n)]
    for x in range(n):
        for y in range(n):
            bd[x][y] /= 100
    mx = 0
    vis = [0]*(n+1)
    find()
    print('#{}'.format(T+1),'%0.6f' % (mx*100))