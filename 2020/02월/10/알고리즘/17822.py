from collections import deque

def rotate(f,c,d):
  for i in range(n):
    if (i+1) % f == 0:
      # print(i)
      if c == 0:
        for j in range(d):
          bd[i].appendleft(bd[i].pop())
      else:
        for j in range(d):
          bd[i].append(bd[i].popleft())

def check():
  global rs
  vis = [[0]*m for i in range(n)]
  target = deque()
  tot = 0
  cnt = 0
  for x in range(n):
    for y in range(m-1):
      if bd[x][y] > 0:
        tot += bd[x][y]
        cnt += 1
      if bd[x][y] == bd[x][y+1] and bd[x][y] > -1:
        if vis[x][y] == 0:
          vis[x][y] = 1
          target.append([x,y])
        if vis[x][y+1] == 0:
          vis[x][y+1] = 1
          target.append([x,y+1])
    if bd[x][m-1] > 0:
      tot += bd[x][m-1]  
      cnt += 1
    if bd[x][0] == bd[x][-1] and bd[x][0] > -1:
      if vis[x][0] == 0:
        target.append([x,0])
        vis[x][0] = 1
      if vis[x][-1] == 0:
        target.append([x,m-1])
        vis[x][-1] = 1
  for y in range(m):
    for x in range(n-1):
      if bd[x][y] == bd[x+1][y] and bd[x][y] > -1:
        if vis[x][y] == 0:
          vis[x][y] = 1
          target.append([x,y])
        if vis[x+1][y] == 0:
          vis[x+1][y] = 1
          target.append([x+1,y])
  if len(target) > 0:
    for x, y in target:
      tot -= bd[x][y]
      bd[x][y] = -1
  else:
    if cnt > 0:
      avg = tot/cnt
      # print(avg)
      for x in range(n):
        for y in range(m):
            if bd[x][y] > avg and bd[x][y] > -1:
              bd[x][y] -= 1
              tot -= 1
            elif bd[x][y] < avg and bd[x][y] > -1:
              bd[x][y] += 1
              tot += 1
    
  rs = tot
  
n,m,t = map(int,input().split())
bd = deque([deque(list(map(int,input().split()))) for i in range(n)])
# print(bd)
for i in range(t):
  f, c, d = map(int,input().split())
  rotate(f,c,d)
  # for i in bd:
  #   print(i)
  check()
  # print('------------')
  # for i in bd:
  #   print(i)
print(rs)