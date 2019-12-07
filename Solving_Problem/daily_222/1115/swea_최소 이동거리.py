from heapq import heappush, heappopfor t in range(1, int(input())+1):
    n,su = map(int,input().split())
    nxt_ls = [[] for i in range(su)]
    for i in range(su):
        s,e,w = map(int,input().split())
        heappush(nxt_ls[s], [w,e])
    q = []
    q.append([0,0])
    dist = [9999999999999999999999999999999]*su
    while q:
        length, point = heappop(q)
        for dt, nxt in nxt_ls[point]:
            if dist[nxt] > length + dt:
                dist[nxt] = length + dt
                heappush(q,[dist[nxt], nxt])
    print(f'#{t} {dist[n]}')
            