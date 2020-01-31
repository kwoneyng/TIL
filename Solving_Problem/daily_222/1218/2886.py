from collections import deque

r,c = map(int, input().split())
bd = [list(input()) for i in range(r)]

for x in range(r):
    for y in range(c):
        if bd[x][y] == 'L':
            search(x,y)