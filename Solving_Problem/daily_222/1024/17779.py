from collections import deque

def selection(x,y,d1,d2):
    global mn
    vis = [[0]*n for i in range(n)]
    rs = 0
    for i in range(n):
        for j in range(n):
            if x+y <= i+j <= x+y+d2*2 and x-y-d1*2 <= i-j <= x-y:
                vis[i][j] = 1
                rs += bd[i][j]
    dp[4] = rs
    rs = 0
    for i in range(x):
        for j in range(y+d1+1):
            if vis[i][j] == 0:
                rs += bd[i][j]
    dp[0] = rs
    rs = 0
    for i in range(x,n):
        for j in range(y+d2):
            if vis[i][j] == 0:
                rs += bd[i][j]
    dp[2] = rs
    rs = 0
    for i in range(x-d1+d2+1):
        for j in range(y+d1+1,n):
            if vis[i][j] == 0:
                rs += bd[i][j]
    dp[1] = rs
    rs = 0
    for i in range(x-d1+d2+1,n):
        for j in range(y+d2,n):
            if vis[i][j] == 0:
                rs += bd[i][j]
    dp[3] = rs
    rs = max(dp) - min(dp)
    if mn > rs :
        mn = rs




n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
mn = 999999999999999999999
dp = [0]*5
for d1 in range(1,n):
    for d2 in range(1,n):
        for x in range(1,n):
            for y in range(1,n):
                if y+d1+d2 < n and x-d1 >= 0 and x+d2 < n:
                    selection(x,y,d1,d2)
print(mn)