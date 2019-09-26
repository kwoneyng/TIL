import heapq
import sys

INF = sys.maxsize

n=int(input())
m=int(input())
nxt_ls=[[] for i in range(n+1)]
costs=[INF]*(n+1)
for i in range(m):
    h_st, h_ed, cost = list(map(int, input().split()))
    nxt_ls[h_st].append((h_ed, cost))
st, ed = list(map(int, input().split()))
costs[st] = 0
q = []
heapq.heappush(q, (0, st))
while q:
    cst, st = heapq.heappop(q)
    for nxt, nxt_cst  in nxt_ls[st]:
        obj_cst = costs[st]+nxt_cst
        if costs[nxt] > obj_cst:
            costs[nxt] = obj_cst
            heapq.heappush(q, (obj_cst, nxt))
print(costs[ed])
