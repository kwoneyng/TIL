from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def start(bd):
    global minute, shark, fish, stop
    vis = [[0]*n for i in range(n)]
    q = deque([shark[0]])
    x,y = shark[0]
    vis[x][y] = 1
    cnt = 0
    while q:
        cnt += 1
        op_xy = [99,99]
        for i in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                a, b = dx[i], dy[i]
                xi, yi = a+x, b+y
                if 0 <= xi < n and 0 <= yi < n and vis[xi][yi] == 0:
                    if 0 < bd[xi][yi] < shark[1] :
                        if op_xy[0] > xi:
                            op_xy = [xi,yi]
                        elif op_xy[0] == xi and op_xy[1] > yi:
                            op_xy = [xi,yi]
                        vis[xi][yi] = 1

                    elif bd[xi][yi] == shark[1] or bd[xi][yi] == 0:
                        q.append([xi,yi])
                        vis[xi][yi] = 1
        if op_xy[0] < 99:
            minute += cnt
            shark[0] = op_xy
            if shark[2] + 1 == shark[1]:
                shark[2] = 0
                shark[1] += 1
            else :
                shark[2] += 1
            bd[op_xy[0]][op_xy[1]] = 0
            fish -= 1
            return

    stop = 1


n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
shark = {}
fish = 0
minute = 0
for x in range(n):
    for y in range(n):
        if bd[x][y] == 9:
            shark[0] = [x,y]
            shark[1] = 2
            shark[2] = 0
            bd[x][y] = 0
        elif 0 < bd[x][y] < 9:
            fish += 1
stop = 0
while fish > 0:
    start(bd)
    if stop == 1:
        break
print(minute)