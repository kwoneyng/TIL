from math import sqrt
from collections import deque

r,c = map(int, input().split())
bd = [list(input()) for i in range(r)]

Lls = deque()
Xls = deque()

for x in range(r):
    for y in range(c):
        if bd[x][y] == 'L':
            Lls.append([x,y])
        elif bd[x][y] == 'X':
            Xls.append([x,y])

nxtls = [[] for i in range(len(Lls))]

for i in range(len(Lls)):
    for j in range(len(Xls)):
        nxtls[i].append()