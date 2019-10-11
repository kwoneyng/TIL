from collections import deque
import sys
input = sys.stdin.readline

near = [(1,0),(0,1),(-1,0),(0,-1)]
m,n = map(int, input().split())
bd = [list(map(int,input().split())) for i in range(n)]
q = deque()
full = m*n
for x in range(n):
    for y in range(m):
        if bd[x][y] == 1:
            q.append([x,y])
            full -= 1
        elif bd[x][y] == -1:
            full -= 1

k = 0
while q:
    flag = 0
    for i in range(len(q)):
        x,y = q.popleft()
        for a,b in near:
            xi, yi = (x+a, y+b)
            if 0 <= xi < n and 0 <= yi < m:
                if bd[xi][yi] == 0:
                    flag = 1
                    q.append([xi,yi])
                    bd[xi][yi] = 1
                    full -= 1
    if flag == 1:
        k += 1
if full != 0:
    print(-1)
else:
    print(k)