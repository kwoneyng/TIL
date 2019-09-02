from pprint import pprint

def bomb(y, ls):
    global h
    for i in range(h):
        if ls[i][y] > 0:
            return i, y, ls


def cross(rs, q):
    global h, w
    x, y, ls = rs
    no = abs(ls[x][y])
    for i in range(no):
        for dx, dy in near:
            if 0 <= x+dx*i< h and 0 <= y+dy*i < w:
                if ls[x+dx*i][y+dy*i] > 1:
                    ls[x+dx*i][y+dy*i] *= -1
                    abc = (x+dx*i, y+dy*i, ls)
                    cross(abc,q)
                if ls[x+dx*i][y+dy*i] != 0:
                    ls[x+dx*i][y+dy*i] = 0
                    q.append((x+dx*i, y+dy*i))
    q.sort(key=lambda x:x[0],reverse=True)
    print(q, len(q))
    while q:
        ck_x, ck_y = q.pop(0)
        if ck_x - 1 >= 0:
            if ls[ck_x-1][ck_y] > 0:
                temp, ls[ck_x-1][ck_y] = ls[ck_x-1][ck_y], 0
                for x_p in range(ck_x, h):
                    if ls[x_p][ck_y] > 0:
                        ls[x_p-1][ck_y] = temp
                        break
                    elif x_p == h-1:
                        ls[x_p][ck_y] = temp
    # pprint(ls)
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
    # while que:
    #     chk = que[0]
    #     dept = chk[0]
    #     if dept == n:
    #         break
    #     ck_bd = chk[1]
    #     que.pop(0)
    #     for y in range(w):
    #         rs = 0
    #         for x in range(h):
    #             rs += ck_bd[x][y]
    #         if rs == 0:
    #             continue
    #         use_bd = [i[:] for i in ck_bd]
    #         que.append([dept+1, cross(bomb(y, use_bd))])
    # for i, ls in que:
    #     rs = 0
    #     for i in ls:
    #         rs += i.count(0)
    #     rs_set.append(w*h - rs)
    # pprint(que)
    # print(min(rs_set))
    pprint(cross((2,2,cross((1,2,bd),q)),q))
    pprint(cross((2,2,cross((1,2,bd),q)),q))
    