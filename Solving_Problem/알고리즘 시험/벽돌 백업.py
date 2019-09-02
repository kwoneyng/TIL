from pprint import pprint

def bomb(y, ls):
    global h
    for i in range(h):
        if ls[i][y] > 0:
            return i, y, ls
    return 0
    


def cross(rs):
    if rs == 0:
        return 0
    global h, w
    x, y, ls = rs
    no = abs(ls[x][y])
    if no == 1:
        ls[x][y] = 0
    else:
        ls[x][y] = 0
        for i in range(1, no):
            for dx, dy in near:
                if 0 <= x+dx*i< h and 0 <= y+dy*i < w:
                    if ls[x+dx*i][y+dy*i] > 1:
                        ls[x+dx*i][y+dy*i] *= -1
                        abc = (x+dx*i, y+dy*i, ls)
                        cross(abc)
                    if ls[x+dx*i][y+dy*i] > 0:
                        ls[x+dx*i][y+dy*i] = 0

    return ls


def down(ls):
    if ls == 0 :
        return 0
    global h, w
    rs = []
    for y in range(w):
        for x in range(h-1,-1,-1):
            if ls[x][y] > 0:
                rs.append(ls[x][y])
                ls[x][y] = 0
        for x in range(h-1,-1,-1):
            if len(rs) == 0:
                break
            ls[x][y] = rs.pop(0)
    return ls



for T in range(1, int(input())+1):
    n, w, h = list(map(int, input().split()))
    bd = []
    for i in range(h):
        bd.append(list(map(int, input().split())))
    que = []
    q = []
    nxt_c = []
    rs_set = []
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    que.append([0, bd])
    while que:
        chk = que[0]
        dept = chk[0]
        if dept == n:
            break
        ck_bd = chk[1]
        que.pop(0)
        for y in range(w):
            rs = 0
            for x in range(h):
                rs += ck_bd[x][y]
            if rs == 0:
                continue
            use_bd = [i[:] for i in ck_bd]
            a = down(cross(bomb(y, use_bd)))
            if a != 0:
                que.append([dept+1, a])
            else :
                que.append([dept+1, 0])
    for i, ls in que:
        if ls == 0:
            continue
        rs = 0
        for i in ls:
            rs += i.count(0)
        rs_set.append(w*h - rs)
    if rs_set == []:
        rs_set = [0, 0]
    print('#{} '.format(T),end='')
    print(min(rs_set))
    