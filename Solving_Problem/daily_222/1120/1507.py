from heapq import heappop, heappush

def go(st,ed):
    q=[]
    heappush(q,[0,st])
    cst = [9999999999]*n
    while q:
        val, node = heappop(q)
        if node == ed:
            cost[st][ed] = val
            return
        for nxt_val, nxt in nxt_ls[node]:
            to_val = val + nxt_val
            if cst[nxt] > to_val:
                heappush(q,[to_val,nxt])
                cst[nxt] = to_val

n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
nxt_ls = [[]for i in range(n)]
for x in range(n):
    for y in range(n):
        if bd[x][y] > 0:
            nxt_ls[x].append([bd[x][y],y])
print(nxt_ls)
cost = [[0]*n for i in range(n)]
vis = [0]*n
for x in range(n):
    for y in range(n):
        go(x,y)

for i in cost:
    print(i)