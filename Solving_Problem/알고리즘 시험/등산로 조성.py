from pprint import pprint

def find(ls, o_vis, dept=1):
    global n
    x, y = ls
    rs_set = []
    rs = 0
    vis = [i[:] for i in o_vis]
    vis[x][y] = 1
    for dx, dy in near:
        X = x+dx
        Y = y+dy
        if 0 <= X < n and 0 <= Y < n:
            if vis[X][Y] == 0:
                if n_bd[X][Y] < n_bd[x][y]:
                    nxt = [X, Y]
                    rs_set.append(find(nxt,vis, dept+1))
    rs_set.append(dept)
    rs = max(rs_set)
    return rs

for T in range(int(input())):
    n, k = map(int, input().split())
    bd = []
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rs_set = []
    for i in range(n):
        bd.append(list(map(int, input().split())))
    chk_set = []
    for x in range(n):
        for y in range(n):
            for z in range(k):
                chk_set.append([x, y, z+1])
    for px, py, z in chk_set:
        n_bd = [i[:] for i in bd]
        o_vis = [[0]*n for j in range(n)]
        max_ls = []
        mx_h = 0
        for x in range(n):
            for y in range(n):
                if n_bd[x][y] > mx_h:
                    mx_h = n_bd[x][y]
        for x in range(n):
            for y in range(n):
                if n_bd[x][y] == mx_h:
                    max_ls.append([x, y])
        n_bd[px][py] -= z            
        for i in max_ls:
            rs_set.append(find(i,o_vis))
    print('#{}'.format(T+1),max(rs_set))