x = int(input())
cs = ['X']*(x+1)
cs[x] = 0
q = [[0, x]]
while q:
    cnt, idx = q.pop(0)
    if idx == 1:
        print(cnt)
        break
    if idx % 2 == 0:
        if cs[idx//2] == 'X':
            cs[idx//2] = cnt+1
            q.append([cnt+1, idx//2])
    if idx % 3 == 0:
        if cs[idx//3] == 'X':
            cs[idx//3] = cnt+1
            q.append([cnt+1, idx//3])
    if cs[idx-1] == 'X':
        cs[idx-1] = cnt +1
        q.append([cnt+1, idx-1])
        
# x = int(input())
# dp = ['X']*(x+1)
# dp[0] = dp[1] = 0
# for i in range(2, x+1):
#     dp[i] = dp[i-1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3]+1)
# print(dp[x])