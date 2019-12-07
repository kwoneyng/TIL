from collections import deque
near = [[-1,0], [0,1], [1,0], [0,-1]]

def burning():
    time = 0
    while fire:
        time += 1
        for i in range(len(fire)):
            x,y = fire.popleft()
            for a,b in near:
                xi, yi = x+a, y+b
                if 0 <= xi < r and 0 <= yi < c:
                    if bd[xi][yi] == '.':
                        bd[xi][yi] = time
                        fire.append([xi,yi])

def escape(bd):
    global rs
    x,y = start
    bd[x][y] = '#'
    q = deque([start])
    time = 0
    while q:
        time += 1
        for i in range(len(q)):
            x,y = q.popleft()
            if x == 0 or y == 0 or x == r-1 or y == c-1:
                rs = time
                return
            for a,b in near:
                xi, yi = x+a, y+b
                if 0 <= xi < r and 0 <= yi < c:
                    if bd[xi][yi] != '#' and bd[xi][yi] != '.' and bd[xi][yi] > time:
                        bd[xi][yi] = '#'
                        q.append([xi,yi])
                    elif bd[xi][yi] == '.':
                        bd[xi][yi] = '#'
                        q.append([xi,yi])


r,c = map(int,input().split())
bd = [list(input()) for i in range(r)]
fire = deque()
rs = 'IMPOSSIBLE'
for x in range(r):
    for y in range(c):
        if bd[x][y] == 'J':
            start = [x,y]
            bd[x][y] = '.'
        elif bd[x][y] == 'F':
            fire.append([x,y])
            bd[x][y] = 0

burning()
escape(bd)
print(rs)