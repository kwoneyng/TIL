near = [[-1,0],[0,1],[1,0],[0,-1]]
from collections import deque

def rotate(x,d,k):
    for i in range(1,n+1):
        if i % x == 0:
            i -= 1
            if d == 0:
                for _ in range(k):
                    a = bd[i].pop()
                    bd[i].insert(0,a)
            else :
                for _ in range(k):
                    bd[i].append(bd[i].pop(0))

def find():
    global flag,total,su
    ls = deque()
    for x in range(n):
        for y in range(m):
            if bd[x][y] > 0:
                total += bd[x][y]
                su += 1
            for a,b in near:
                xi, yi = x+a,y+b
                if 0 <= xi < n and 0 <= yi < n:
                    if bd[x][y] == bd[xi][yi] and bd[x][y] > 0:
                        ls.append([x,y])
        if bd[x][0] == bd[x][m-1] and bd[x][0] != 0:
            ls.append([x,0])
            ls.append([x,m-1])
    if ls:
        flag = 1
    for x,y in ls:
        bd[x][y] = 0

n,m,t = map(int,input().split())
bd = [list(map(int, input().split())) for i in range(n)]
data = deque()
for i in range(t):
    data.append(list(map(int,input().split())))

for x,d,k in data:
    flag = 0
    total = 0
    su = 0
    rotate(x,d,k)
    find()
    if flag == 0:
        if su != 0:
            mid = total / su 
            for x in range(n):
                for y in range(m):
                    if 0 < bd[x][y] < mid:
                        bd[x][y] += 1
                    elif bd[x][y] > mid:
                        bd[x][y] -= 1
rs = 0
if su == 0:
    print(0)
else:
    for i in bd:
        rs += sum(i)
    print(rs)