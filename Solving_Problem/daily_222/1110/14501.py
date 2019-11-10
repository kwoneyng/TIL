n = int(input())
dt = []
pt = []
dp = [0]*21
for i in range(n):
    day, pay = map(int, input().split())
    dp[i+1] = max(dp[i],dp[i+1])
    dp[i+day] = max(dp[i] + pay, dp[i+day])
print(dp[n])