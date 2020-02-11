from heapq import heappop, heappush

near=[[-1,0],[0,1],[1,0],[0,-1]]

def marking(x,y):
  bd[x][y] = cnt
  for a,b in near:
    xi,yi = a+x, y+b
    if 0<=xi<n and 0<=yi<m and bd[xi][yi] == 1:
      marking(xi,yi)

n, m = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]
cnt = -1
ht={}
for x in range(n):
  for y in range(m):
    if bd[x][y] == 1:
      marking(x,y)
      cnt -= 1
for x in range(n):
  st,dt = 0,0
  for y in range(m):
    if st == 0:
      if bd[x][y] < 0:
        st = -bd[x][y]
    elif bd[x][y] == 0:
      dt += 1
    elif bd[x][y] < 0:
      if dt > 1:
        if st < -bd[x][y]:
          if ht.get((st,-bd[x][y])):
            ht[(st,-bd[x][y])] = min(dt,ht[(st,-bd[x][y])])
          else:
            ht[(st,-bd[x][y])] = dt
        else:
          if ht.get((-bd[x][y],st)):
            ht[(-bd[x][y],st)] = min(dt,ht[(-bd[x][y],st)])
          else:
            ht[(-bd[x][y],st)] = dt
      st = -bd[x][y]
      dt = 0

for y in range(m):
  st,dt = 0,0
  for x in range(n):
    if st == 0:
      if bd[x][y] < 0:
        st = -bd[x][y]
    elif bd[x][y] == 0:
      dt += 1
    elif bd[x][y] < 0:
      if dt > 1:
        if st < -bd[x][y]:
          if ht.get((st,-bd[x][y])):
            ht[(st,-bd[x][y])] = min(dt,ht[(st,-bd[x][y])])
          else:
            ht[(st,-bd[x][y])] = dt
        else:
          if ht.get((-bd[x][y],st)):
            ht[(-bd[x][y],st)] = min(dt,ht[(st,-bd[x][y])])
          else:
            ht[(-bd[x][y],st)] = dt
      st = -bd[x][y]
      dt = 0

# print(ht)

cost = [9999]*(-cnt)
nxtls=[[]for i in range(-cnt)]
for key,v in ht.items():
  x,y = key
  nxtls[x].append([v,y])
  nxtls[y].append([v,x])

cost = [9999]*(-cnt)
cost[0] = 0
cost[1] = 0
vis = [0]*(-cnt)
q = [[0,1]]
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

print(cost)
rs = sum(cost)
if rs > 300:
  print(-1)
else:
  print(sum(cost))