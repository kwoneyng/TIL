def go(n):
    if n == 1:
        dp[n] = 1
    elif n == 2:
        dp[n] = 2
    elif n == 3:
        dp[n] = 4
    else:
        dp[n] = go(n-3) + go(n-2) + go(n-1)
    return dp[n]

for t in range(int(input())):
    n = int(input())
    dp = [0]*12
    go(n)
    print(dp[n])