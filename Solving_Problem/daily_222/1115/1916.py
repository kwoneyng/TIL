from heapq import heappop, heappush

def dijk(st, ed):
    q = []
    q.append([0,st])
    while q:
        val, point = heappop(q)
        if point == ed:
            print(val)
            return
        else:
            for nxt_val, nxt in nxt_ls[point]:
                to_val = nxt_val+val
                if to_val < cost[nxt]:
                    heappush(q,[to_val, nxt])
                    cost[nxt] = to_val


n = int(input())
m = int(input())
nxt_ls = [[]for i in range(n+1)]
cost = [99999999999999999999999999999]*(n+1)
cost[0], cost[1] = 0,0
for i in range(m):
    s,e,v = map(int,input().split())
    nxt_ls[s].append([v,e])
st, ed = map(int,input().split())
dijk(st, ed)