from heapq import heappop, heappush
from collections import deque


def go():
    global rs
    q = deque()
    q.append(1)
    cnt = 1
    while q:
        cnt += 1
        for i in range(len(q)):
            point = q.popleft()
            for nxt in nxt_ls[point]:
                if nxt == n:
                    rs = cnt
                    return
                elif vis[nxt] == 0:
                    vis[nxt] = 1
                    q.append(nxt)

n,k,m = map(int,input().split())
nxt_ls = [set() for i in range(n+1)]
vis = [0]*(n+1)
rs = 0
for i in range(1,m+1):
    a,b,c = list(map(int,input().split()))
    nxt_ls[a].add(b)
    nxt_ls[a].add(c)
    nxt_ls[b].add(a)
    nxt_ls[b].add(c)
    nxt_ls[c].add(a)
    nxt_ls[c].add(b)
go()
if rs == 0:
    print(-1)
else:
    print(rs)