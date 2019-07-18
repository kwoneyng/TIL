def valid_sqr(a, b):
    val_hel = []
    val = {}
    for i in range(a, a+3):
        for j in range(b, b+3):
            val_hel.append(XY[i][j])
    val = set(val_hel)
    if len(val) == 9:
        return 1
    else :
        return 0


def valid_line(a, b):
    val_hel = []
    val = {}
    if a == 0 :
        for i in range(9):
            val_hel.append(XY[i][b])
    elif a == 1 :
        for i in range(9):
            val_hel.append(XY[b][i])
    val = set(val_hel)
    if len(val) == 9:
        return 1
    else : 
        return 0



test_num = int(input())
for i in range(test_num):
    XY = []
    rs = []
    rl_X = []
    rl_Y = []
    result = 0
    for j in range(9) :
        XY.append(list(map(int, input().split())))
    for j in (0, 3, 6):
        for k in (0, 3, 6):
            rs.append(valid_sqr(j, k))
    for j in range(2):
        for k in range(9):
            rs.append(valid_line(j, k))
    if 0 in rs :
        result = 0
    else :
        result = 1
    print(f'#{i+1} {result}')
