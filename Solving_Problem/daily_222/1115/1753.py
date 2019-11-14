from heapq import heappop, heappush
import sys
input = sys.stdin.readline


v,e = map(int,input().split())
k = int(input())
nxt_ls = [[] for i in range(v+1)]
for i in range(e):
    x,y,w = map(int,input().split())
    nxt_ls[x].append([w,y])
cost = [99999999999999999999999999]*(v+1)
cost[0] = 0
cost[k] = 0
q = []
q.append([0,k])
while q:
    val, point = heappop(q)
    for nxt_val, nxt in nxt_ls[point]:
        if cost[nxt] > val+nxt_val:
            cost[nxt] = val+nxt_val
            heappush(q, [val + nxt_val, nxt])

for i in range(1,v+1):
    if cost[i] > 9999999999999999999999999:
        print('INF')
    else :
        print(cost[i])
