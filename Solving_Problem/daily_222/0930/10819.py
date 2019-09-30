def go(vis=[]):
    global mx
    if len(vis) == n:
        rs = 0
        for i in range(n-1):
            rs += abs(ls[vis[i]] - ls[vis[i+1]])
        if rs > mx:
            mx = rs

    for i in range(n):
        if i not in vis:
            go(vis+[i])



n = int(input())
ls = [i for i in list(map(int,input().split()))]
mx = 0
go()
print(mx)