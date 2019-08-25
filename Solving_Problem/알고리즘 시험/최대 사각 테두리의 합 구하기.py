def sp_sum(start_x, start_y):
    global k
    rs = 0
    for i in range(start_y, start_y+k):
        rs += bd[start_x][i]
    for j in range(start_x+1, start_x+k):
        rs += bd[j][start_y]
        rs += bd[j][start_y+k-1]
    for l in range(start_y+1, start_y+k-1):
        rs += bd[start_x+k-1][l]
    return rs


for T in range(int(input())):
    n, m, k = map(int, input().split())
    bd = []
    for i in range(n):
        bd.append(list(map(int, input().split())))
    rs_set = []
    for i in range(n-k+1):
        for j in range(m-k+1):
            rs_set.append(sp_sum(i,j))

    print('#{} '.format(T+1),end='')
    print(max(rs_set))