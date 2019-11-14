from collections import deque
from math import sqrt
from heapq import heappop, heappush


def prim():
    ls = []
    ls.append([0,0])
    while ls:
        val, nxt = heappop(ls)
        if vis[nxt] == 0:
            vis[nxt] = 1
            for val, nxt in nxt_ls[nxt]:
                if vis[nxt] == 0:
                    cost[nxt] = min(cost[nxt], val)
                    heappush(ls,[val,nxt])

for t in range(int(input())):
    n = int(input())
    nxt_ls = [[] for i in range(n+1)]
    q = deque()
    dtx = list(map(int, input().split()))
    dty = list(map(int, input().split()))
    tax = float(input())
    cost = [999999999999999999]*n
    cost[0] = 0
    vis = [0]*n
    for x in range(n):
        for y in range(x+1, n):
            val = tax * ((dtx[x]-dtx[y])**2 + (dty[x]-dty[y])**2)
            nxt_ls[x].append([val,y])
            nxt_ls[y].append([val,x])
    prim()
    a = sum(cost)
    rs = int(a*2) - int(a)
    print(f'#{t+1} {rs}')