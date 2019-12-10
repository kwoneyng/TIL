from heapq import heappop,heappush

def go(start = 0):
    q = [[0,0,0]] # 환승 횟수, 비용, 노드
    vis = [0]*n
    vis[0] = 1
    cst = [9999999999999]*n
    while q:
        hwan, cost, node = heappop(q)
        vis[node] = 1
        if node == m:
            print(hwan, cost)
            return
        for i in range(len(bd[node])):
            if vis[i] == 0:
                if bd[node][i] > 0:
                    if cst[i] > cost+bd[node][i]:
                        cst[i] = cost+bd[node][i]
                        if company[i] != company[node]:
                            heappush(q,[hwan+1, cost+bd[node][i], i])
                        else:
                            heappush(q,[hwan, cost+bd[node][i], i])


n,m = map(int,input().split())
company = []
for i in range(n):
    company.append(int(input()))

bd=[list(map(int, input().split())) for i in range(n)]
go()