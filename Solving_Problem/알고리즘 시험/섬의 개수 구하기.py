def go():
    global cnt
    for x in range(n):
        for y in range(n):
            if vis[x][y] == 0:
                vis[x][y] = 1
                if bd[x][y] >= 1:
                    cnt += 1
                    return cnt_land(x, y)

            
def cnt_land(st_x, st_y):
    for x, y in near:
        if 0 <= st_x+x < n and 0 <= st_y+y < n:
            if vis[st_x+x][st_y+y] == 0:
                vis[st_x+x][st_y+y] = 1
                if bd[st_x+x][st_y+y] > 0:
                    bd[st_x+x][st_y+y] = cnt
                    cnt_land(st_x+x, st_y+y)


def com_vis():
    rs = 0
    for i in vis:
        rs += i.count(0)
    if rs == 0:
        return False
    else:
        return True

for T in range(int(input())):
    n = int(input())
    bd = []
    vis = []
    cnt = 0
    near = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for i in range(n):
        vis.append([0 for i in range(n)])
    for i in range(n):
        bd.append(list(map(int, input().split())))
    while com_vis():
        go()
    print('#{} '.format(T+1),end='')
    print(cnt)