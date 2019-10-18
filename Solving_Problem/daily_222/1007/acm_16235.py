from collections import deque
from heapq import heappop,heappush

near = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def year():
    spr()
    sm()
    f()
    wt()

def spr():
    for x in range(1,n+1):
        for y in range(1,n+1):
            for j in range(len(bd[x][y])):
                z = bd[x][y].popleft()
                if c_bd[x][y] >= z:
                    c_bd[x][y] -= z
                    bd[x][y].append(z+1)
                else:
                    dethree.append([x,y,z])


def sm():
    for i in range(len(dethree)):
        x,y,z = dethree.popleft()
        c_bd[x][y] += z//2
    

def f():
    for x in range(1,n+1):
        for y in range(1,n+1):
            for j in range(len(bd[x][y])):
                if bd[x][y][j] % 5 == 0:
                    for a,b in near:
                        xi,yi = x+a, y+b
                        if 0 < xi <= n and 0 < yi <= n:
                            bd[xi][yi].appendleft(1)
    

def wt():
    for x in range(1,n+1):
        for y in range(1,n+1):
            c_bd[x][y] += a_bd[x][y]



n,m,k = map(int,input().split())
a_bd = [[0]*(n+1)]
for i in range(n):
    a_bd.append([0]+list(map(int,input().split())))
dethree = deque()
bd = [[deque() for i in range(n+1)] for i in range(n+1)]
c_bd = [[5]*(n+1) for i in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    bd[x][y].append(z)

for i in range(k):
    year()
rs = 0
for x in range(1,n+1):
    for y in range(1,n+1):
        rs += len(bd[x][y])

print(rs)