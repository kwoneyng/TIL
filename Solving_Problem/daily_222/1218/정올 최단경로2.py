from heapq import heappop,heappush
import sys
input = sys.stdin.readline

def rootfind(x=1):
    q = [[0,1]]
    while q:
        val, node = heappop(q)
        if node == n:
            print(val)
            return
        if dp[node] == -1:
            dp[node] = val
        for nval, nxt in nxtls[node]:
            toval = nval+val
            if dp[nxt] == -1:
                heappush(q,[toval,nxt])

n, m = map(int,input().split())
nxtls = [[]for i in range(n+1)]
dp = [-1]*(n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    nxtls[a].append([c,b])
rootfind()