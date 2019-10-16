from collections import deque

for t in range(int(input())):
    n,m = map(int,input().split())
    dp = [0]*(1000001)
    dp[n] = 1
    q = deque([[n,0]])
    while q:
        nn,cnt = q.popleft()
        if nn == m:
            break
        if nn+1 < 1000001:
            if dp[nn+1] == 0:
                dp[nn+1] = 1
                q.append([nn+1,cnt+1])
        if nn-1 > 0:
            if dp[nn-1] == 0:
                dp[nn-1] = 1
                q.append([nn-1,cnt+1])
        if nn*2 < 1000001:
            if dp[nn*2] == 0:
                q.append([nn*2,cnt+1])
        if nn-10 > 0:
            if dp[nn-10] == 0:
                dp[nn-10] = 1
                q.append([nn-10,cnt+1])
    print('#{}'.format(t+1),cnt)
