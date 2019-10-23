import heapq

n = int(input())
m = int(input())
data = []
nxt_ls = [[] for i in range(n+1)]
cost = [0]+[10000]*n
cost[1] = 0
vis = [0]*(n+1)
for i in range(m):
    a,b,c = list(map(int,input().split()))
    nxt_ls[a].append([b,c])
    nxt_ls[b].append([a,c])
q = [[0,1]]
while q:
    pay, no = heapq.heappop(q)
    if vis[no] != 0:
        continue
    vis[no] = 1
    for nno, npay in nxt_ls[no]:
        if vis[nno] == 0:
            if cost[nno] > npay:
                cost[nno] = npay
            heapq.heappush(q,[npay,nno])
print(sum(cost))