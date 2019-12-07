<<<<<<< HEAD
n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
can = [[1]*n for i in range(n)]

rs = 0

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x != k and y != k and x != y:
                if bd[x][y] == bd[x][k] + bd[k][y]:
                    can[x][y] = 0
                elif bd[x][y] > bd[x][k] + bd[k][y]:
                    rs = -1
        else:
            continue
        break
    else:
        continue
    break
# for i in can:
#     print(i)

if rs == 0:
    for x in range(n):
        for y in range(x,n):
            if can[x][y] == 1:
                rs += bd[x][y]
    print(rs)
else:
    print(rs)
=======
from heapq import heappop, heappush

n = int(input())
path = [0]*(1000002)
for i in range(n):
    a,b = map(int,input().split())
    path[a] = b
l,p = map(int,input().split())
cnt = 0
q = []
for i in range(1,l+1):
    p -= 1
    if p < 0:
        while q:
            p -= heappop(q)
            cnt += 1
            if p >= 0:
                break
        else:
            if p < 0:
                print(-1)
                break
    if path[i] > 0:
        heappush(q,-path[i])
else:
    print(cnt)
>>>>>>> 77a3418d465bc078d587a6ab98487cae439e30c6
