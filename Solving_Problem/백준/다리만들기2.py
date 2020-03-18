from heapq import heappop, heappush

near = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def marking(x, y):
    bd[x][y] = cnt
    for a, b in near:
        xi, yi = a+x, y+b
        if 0 <= xi < n and 0 <= yi < m and bd[xi][yi] == 1:
            marking(xi, yi)


n, m = map(int, input().split())
bd = [list(map(int, input().split())) for i in range(n)]
cnt = -1
ht = {}
for x in range(n):
    for y in range(m):
        if bd[x][y] == 1:
            marking(x, y)
            cnt -= 1


for x in range(n):
    st, dt = -1, 0
    for y in range(m):
        if st < 0:  # 아직 섬을 못 만났을 때
            if bd[x][y] < 0:  # 섬을 만나면
                st = (-bd[x][y]) - 1
        elif bd[x][y] < 0 and -(bd[x][y]+1) != st:
            if dt > 1: # 섬을 만났는데 시작섬과 다르면 (섬간 거리 2 이상)
                target = (min(st,-(bd[x][y]+1)),max(-(bd[x][y]+1),st))
                if ht.get(target):
                    ht[target] = min(dt, ht[target])
                    st = -bd[x][y] - 1
                    dt=0
                else:
                    ht[target] = dt
                    st = -bd[x][y] - 1
                    dt=0
            else:
                st = -bd[x][y]-1
                dt = 0
        elif bd[x][y] == 0:
            dt += 1

for y in range(m):
    st,dt = -1,0
    for x in range(n):
        if st < 0: # 아직 섬을 못 만났을 때
            if bd[x][y] < 0: # 섬을 만나면
                st = (-bd[x][y]) - 1
        elif bd[x][y] < 0 and -(bd[x][y]+1) != st: 
            if dt > 1: # 섬을 만났는데 시작섬과 다르면 (섬간 거리 2 이상)
                target = (min(st,-(bd[x][y]+1)),max(-(bd[x][y]+1),st))
                if ht.get(target):
                    ht[target] = min(dt, ht[target])
                    st = -bd[x][y] - 1
                    dt=0
                else:
                    ht[target] = dt
                    st = -bd[x][y] - 1
                    dt=0
            else:
                st = -bd[x][y] - 1
                dt=0
        elif bd[x][y] == 0:
            dt += 1

# for i in bd:
#     print(i)

# print(ht)




cost = [9999]*(-cnt)
nxtls=[[]for i in range(-cnt-1)]
for key,v in ht.items():
    x,y = key
    nxtls[x].append([v,y])
    nxtls[y].append([v,x])

cost = [9999]*(-cnt-1)
cost[0] = 0
vis = [0]*(-cnt-1)
q = [[0,0]]
while q:
    v, node = heappop(q)
    if vis[node] != 0:
        continue
    vis[node] = 1
    for nv, nxt in nxtls[node]:
        if vis[nxt] == 0:
            if cost[nxt] > nv:
                cost[nxt] = nv
                heappush(q,[nv,nxt])

# for i in bd:
#     print(i)
# print(nxtls)
# print(ht)
# print(cost)
rs = sum(cost)

if rs > 9999:
    print(-1)
else:
    print(rs)
