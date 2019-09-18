V,E = map(int, input().split())
start = int(input())
nxt_ls = {i : {} for i in range(1,V+1)}
costs = {i : 'inf' for i in range(1, V+1)}
costs[start] = 0
q = [(start,0)]
for i in range(E):
    u,v,w = list(map(int, input().split()))
    nxt_ls[u][v] = w
while q:
    chk, cost = q.pop()
    for nxt, nxt_cost in nxt_ls[chk].items(): # 다음에 갈 애들
        q.append([nxt, cost+nxt_cost])
        if costs[nxt] == 'inf':
            costs[nxt] = nxt_cost+cost
        elif costs[nxt] > nxt_cost+cost:
            costs[nxt] = nxt_cost+cost
for i in range(1,V+1):
    print(costs[i])