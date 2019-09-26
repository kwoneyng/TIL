import sys
from heapq import heappop, heappush

n, m, x = map(int, input().split())
nls = [[] for i in range(n+1)]
rvls = [[] for i in range(n+1)]
for i in range(m):
    st, ed, tm = map(int, input().split())
    nls[st].append((ed,tm))
    rvls[ed].append((st,tm))
print(nls)
print(rvls)
spend = [0]*(n+1)
st_p = x
q = [(0,x)]
while q:
    cst, here = heappop(q)
    for i in nls[here]:
        
