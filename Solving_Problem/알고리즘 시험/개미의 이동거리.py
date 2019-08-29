def W1():
    global fw, x, y, cnt, n
    if fw == 0:
        fw = 3
        x -= 1
        if x - 1 >= 0 :
            cnt += 1
    elif fw == 1:
        fw = 2
        y -= 1
        if y - 1 >= 0 :
            cnt += 1 
    elif fw == 2:
        fw = 1
        x += 1
        if x + 1 < n:
            cnt += 1
    elif fw == 3:
        fw = 0
        y += 1
        if y + 1 < n:
            cnt += 1
    

def W2():
    global fw, x, y, cnt, n
    if fw == 0:
        fw = 1
        x += 1
        if x + 1 < n:
            cnt += 1
    elif fw == 1:
        fw = 0
        y += 1
        if y+1 < n:
            cnt += 1
    elif fw == 2:
        fw = 3
        x -= 1
        if x-1 >= 0:
            cnt +=1
    elif fw == 3:
        fw = 2
        y -= 1
        if y-1 >= 0:
            cnt +=1

for T in range(int(input())):
    n = int(input())
    bd = []
    fw = 0
    for i in range(n):
        bd.append(list(map(int, input().split())))
    x, y = [0, 0]
    cnt = 0
    chk_end = False
    while 0 <= x < n and 0 <= y < n :
        if chk_end:
            break
        elif fw == 0:
            while bd[x][y] != 1 and bd[x][y] != 2:
                if y + 1 < n :
                    cnt += 1
                    y += 1
                else :
                    y += 1
                    chk_end = True
                    break
            if bd[x][y] == 1:
                W1()
            elif bd[x][y] == 2:
                W2()
        elif fw == 1:
            while bd[x][y] != 1 and bd[x][y] != 2:
                if x + 1 < n :
                    cnt += 1
                    x += 1
                else :
                    x += 1
                    chk_end = True
                    break
            if bd[x][y] == 1:
                W1()
            elif bd[x][y] == 2:
                W2()
        elif fw == 2:
            while bd[x][y] != 1 and bd[x][y] != 2:
                if y - 1 >= 0 :
                    cnt += 1
                    y -= 1
                else :
                    y -= 1
                    chk_end = True
                    break
            if bd[x][y] == 1:
                W1()
            elif bd[x][y] == 2:
                W2()
        elif fw == 3:
            while bd[x][y] != 1 and bd[x][y] != 2:
                if x - 1 >= 0 :
                    cnt += 1
                    x -= 1
                else :
                    x -= 1
                    chk_end = True
                    break
            if bd[x][y] == 1:
                W1()
            elif bd[x][y] == 2:
                W2()
    print(cnt)
# 1
# 10
# 0 0 0 0 0 0 0 2 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 0 1 0 1 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 2 0 0 1 0 0 1 0 0
# 0 0 0 0 2 0 0 2 0 0
# 1 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 1 2 0 0 0 0 1 1 0
# 0 0 0 0 0 2 0 0 0 0
