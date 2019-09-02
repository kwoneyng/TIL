from pprint import pprint

def bomb(y):
    global h
    for i in range(h):
        if vis[i][y] == 0:
            vis[i][y] = 1
            if bd[i][y] >= 1:
                cross(i, y)
                break


def cross(x, y):
    global cnt, h, w
    a = bd[x][y]
    bd[x][y] = 0
    cn = -1
    pprint(bd)
    while a >= 1:
        a -= 1
        cn += 1
        for dx, dy in near:
            if 0 <= x+dx*cn < h and 0 <= y+dy*cn < w:
                if vis[x+dx*cn][y+dy*cn] == 0:
                    vis[x+dx*cn][y+dy*cn] = 1
                    if bd[x+dx*cn][y+dy*cn] > 1:
                        cross(x+dx*cn, y+dy*cn)
                    if bd[x+dx*cn][y+dy*cn] != 0:
                        bd[x+dx*cn][y+dy*cn] = 0
                        cnt += 1
                        q.append((x+dx, y+dy))


def start():
    global h
    q.sort(key=lambda x:x[0], reverse=True)
    for i in range(len(q)):
        x, y = q[i]
        if x - 1 >= 0:
            if bd[x-1][y] > 0:
                temp, bd[x-1][y] = bd[x-1][y], 0
                while True :
                    x += 1
                    if bd[x][y] != 0:
                        bd[x-1][y] = temp
                        break
                    elif x == h-1:
                        bd[x][y] = temp


for T in range(int(input())):
    n, w, h = list(map(int, input().split()))
    bd = []
    q = []
    vis = []
    cnt = 0 # 위치 변경 필요
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(h):
        bd.append(list(map(int, input().split())))
        vis.append([0 for i in range(w)])
    bomb(2)
    bomb(2)
    pprint(bd)