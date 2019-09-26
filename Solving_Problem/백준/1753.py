import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solve(nxt_ls, start):
    costs = [INF] * (len(nxt_ls))
    costs[start] = 0

    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        cost, chk = heapq.heappop(q)
        for nxt, nxt_cost in nxt_ls[chk].items(): # 다음에 갈 애들
            th_cost = nxt_cost+cost
            if costs[nxt] > th_cost:
                costs[nxt] = th_cost
                heapq.heappush(q,[th_cost, nxt])
    return costs

V,E = map(int, input().split())
start = int(input())
nxt_ls = [{} for i in range(V+1)]
for i in range(E):
    u,v,w = list(map(int, input().split()))
    if v in nxt_ls[u]:
        nxt_ls[u][v] = min(nxt_ls[u][v],w)
    else:
        nxt_ls[u][v] = w
costs = solve(nxt_ls,start)

for i in costs[1:]:
    print(i if i != INF else 'INF')