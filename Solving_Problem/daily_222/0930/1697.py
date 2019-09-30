def go(x,cnt=0):
    dp[x] = cnt
    if 0 <= x-1 < 100001:
        if dp[x-1] == -1:
            go(x-1,cnt)
    if 0 <= x+1 < 100001:
        if dp[x+1] == -1:    
            go(x+1,cnt)
    if 0 <= 2*x < 100001:
        if dp[2*x] == -1:
            go(2*x,cnt)



n, m = map(int, input().split())
dp = [-1]*100001
go(n)
print(dp[m])