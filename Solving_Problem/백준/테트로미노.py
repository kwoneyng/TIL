def straight(x, y):
    global n, m
    su_1 = 0
    for i in range(4):
        if 0 <= y+i < n:
            su_1 += bd[x][y+i]
    su_2 = 0
    for i in range(4):
        if 0 <= x+i < n:
            su_2 += bd[x+i][y]
    print(x, y, max(su_1, su_2), 'st')
    return max(su_2, su_1)


def L_form(x, y):
    global n,m
    su_1 = 0
    su_2 = 0
    su_3 = 0
    su_4 = 0
    for i in range(3):
        if 0 <= x+i < n:
            su_1 += bd[x+i][y]
        else :
            su_1 = 0
    if 0 <= y+1 < n and 0 <= x+2 < n:
        su_1 += bd[x+2][y+1]
    else :
        su_1 = 0
    
    for i in range(3):
        if 0 <= y+i < n:
            su_2 += bd[x][y+i]
        else:
            su_2 = 0
    if 0 <= x+1 < n:
        su_2 += bd[x+1][y]
    else :
        su_2 = 0
    
    for i in range(3):
        su_3 += bd[x][y]
        if 0 <= y+1 < n and 0 <= x+i < n:
            su_3 += bd[x+i][y+1]
        else :
            su_3 = 0
    
    for i in range(3):
        if 0 <= y+i < n and 0 <= x+1 < n:
            su_4 += bd[x+1][y+i]
        else :
            su_4 = 0
    if 0 <= y+2 < n:
        su_4 += bd[x][y+2]
    else :
        su_4 = 0
    print(x, y, max(su_1,su_2,su_3,su_4), 'L')
    return max(su_1, su_2, su_3, su_4)
    
            


n, m = map(int, input().split())
bd = [list(map(int, input().split())) for i in range(n)]
to_ls = []
for x in range(n):
    for y in range(m):
        to_ls.append(straight(x, y))
        to_ls.append(L_form(x, y))
print(to_ls)
