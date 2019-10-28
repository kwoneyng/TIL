from collections import deque

def select(x,y,d1,d2):
    vis = [[0]*n for i in range(n)]
    q = deque()
    rs = 0
    vis[x][y] = 1
    rs += bd[x][y]
    q.append([x,y])
    vis[x+d2][y+d2] = 1
    rs += vis[x+d2][y+d2]
    vis[x-d1][y+d1] = 1
    rs += vis[x-d1][y+d1]
    vis[x-d1+d2][y+d1+d2] = 1
    rs += vis[x-d1+d2][y+d1+d2]

    while True:
        x += 1
        y += 1
        if vis[x][y] == 0:
            rs += bd[x][y]
            vis[x][y] = 1
            q.append([x,y])
        else:
            break
    while True:
        x -= 1
        y += 1
        if vis[x][y] == 0:
            vis[x][y] = 1
            rs += bd[x][y]
        else:
            break
    while True:
        x -= 1
        y -= 1
        if vis[x][y] == 0:
            vis[x][y] = 1
            rs += bd[x][y]
        else:
            break
    while True:
        x += 1
        y -= 1
        if vis[x][y] == 0:
            vis[x][y] = 1
            q.append([x,y])
            rs += bd[x][y]
        else:
            break
    
    for x,y in q:
        while True:
            y += 1
            if vis[x][y] == 0:
                vis[x][y] = 1
                rs += bd[x][y]
            else:
                break
    for i in vis:
        print(i)
    print("-------")
    dp[4] = rs
    for i in range(x):
        for j in range(y+1):
    for i in range(x+1):
        for j in range(y+1,n):
    for i in range(x,n):
        for j in range(y):
    for i in range(x+1,n):
        for j in range():



n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]

d_set = deque()
for i in range(1,n-1):
    for j in range(1,n-1):
        d_set.append([i,j])

dp = [0]*5
for d1,d2 in d_set:
    for x in range(n):
        for y in range(n):
            if x-d1 >= 0 and x+d2 < n and y+d1+d2 < n:
                select(x,y,d1,d2)