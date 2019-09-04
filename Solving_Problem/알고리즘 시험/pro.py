from pprint import pprint

for T in range(int(input())):
    n = int(input())
    bd = []
    cnt = 0
    for i in range(n):
        bd.append(list(map(int,input().split())))
    stack = []
    while True:
        end = 0
        for x in range(n):
            for y in range(n):
                if bd[x][y] != 0 :
                    stack.append([x,y])
                    cnt += 1
                    end = 1
                    break 
            if end:
                break
        if end == 0:
            break
        x, y = stack.pop(0)
        c_r, c_c = 1, 1
        y_break = 0
        fin = 0
        while True:
            if fin:
                break
            if not y_break:
                y += 1
            else :
                x += 1
            if not y_break:
                if y == n-1 :
                    y_break = 1
                    y -= 1
            elif x == n-1 :
                fin = 1
                x -= 1

            elif bd[x][y] == 0:
                if not y_break:
                    y_break = 1
                    y -= 1
                else :
                    fin = 1
                    x -= 1
            else :
                if not y_break:
                    c_c += 1
                else :
                    c_r += 1
        print(c_r, c_c, x, y)
        for i in range(x,x-c_r,-1):
            for j in range(y, y-c_c, -1):
                bd[i][j] = 0
        pprint(bd)
