from collections import deque
from random import random

def div_con(x,s,e,dp,ht):
    global length
    if s > e:
        if s > length:
            dp.append(als[x])
            ht[als[x]] = dp[length]
            length += 1
            return
        dp[s] = als[x]
        if s > 0:
            ht[dp[s]] = dp[s-1]
        return
    else:
        m = (s+e)//2
        if als[x] > dp[m]:
            div_con(x,m+1,e,dp,ht)
        elif als[x] < dp[m]:
            div_con(x,s,m-1,dp,ht)

def back(x):
    if ht.get(x):
        rs.appendleft(str(ht[x]))
        back(ht[x])


n = int(input())
als = list(map(int,input().split()))
length = 0
dp = [als[0]]
ht = {}
for i in range(1,n):
    div_con(i,0,length,dp,ht)
rs = deque([str(dp[-1])])
back(dp[-1])
print(length+1)
print(' '.join(rs))
