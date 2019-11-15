from heapq import heappop, heappush

def go():
    q = []
    heappush(q,[1,1])
    while q:
        cnt, point = heappop(q)
        for nxt in nxt_ls[point]:
            ncnt = cnt + 1
            if vis[nxt] > ncnt:
                vis[nxt] = ncnt
                heappush(q,[ncnt,nxt])

n,k,m = map(int,input().split())
nxt_ls = [[] for i in range(n+1)]
vis = [999999999999999999999999]*(n+1)
for i in range(1,m+1):
    data = list(map(int,input().split()))
    nxt_ls[i].extend(data)
go()
if vis[n] >= 999999999999999999999999:
    print(-1)
else:
    print(vis[n])