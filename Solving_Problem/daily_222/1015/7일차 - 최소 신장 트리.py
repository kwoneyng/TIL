from heapq import heappop, heappush

for t in range(int(input())):
    v,e = map(int,input().split())
    vis = [0]*(v+1)
    nxt_ls = [[] for i in range(v+1)]
    cost = [999999999999999999]*(v+1)
    q = [(0,0)]
    cost[0] = 0
    for i in range(e):
        n1,n2,val = list(map(int,input().split()))
        heappush(nxt_ls[n1],(val,n2))
        heappush(nxt_ls[n2],(val,n1))

    while q:
        val, st = heappop(q)
        vis[st] = 1
        for val, ed in nxt_ls[st]:
            if vis[ed] == 0:
                if cost[ed] > val:
                    cost[ed] = val
                    heappush(q,(val,ed))
    print('#{}'.format(t+1),sum(cost))
    