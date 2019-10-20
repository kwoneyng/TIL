def go(dp, rs = 0, idx = 0):
    global cnt
    if idx == n:
        if dp[idx].get(rs) == None:
            dp[idx][rs] = 1
            cnt += 1
            return
    if dp[idx].get(rs) == None:
        dp[idx][rs] = 1
        go(dp, rs+score[idx], idx+1)
        go(dp, rs, idx+1)
    elif dp[idx].get(rs) != None:
        return

for t in range(int(input())):
    n = int(input())
    dp = [{} for i in range(n+1)]
    score = list(map(int, input().split()))  
    cnt = 0
    go(dp)
    print('#{}'.format(t+1), cnt)