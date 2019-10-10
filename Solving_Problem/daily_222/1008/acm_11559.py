near = [[0,1],[1,0],[-1,0],[0,-1]]
def go_down():
    for y in range(6):
        down = []
        for x in range(12):
            if bd[x][y] != '.':
                down.append(bd[x][y])
                bd[x][y] = '.'
        for x in range(11,-1,-1):
            if down:
                bd[x][y] = down.pop()
            else:
                break
def go_puyo(x,y,clr):
    for dx, dy in near:
        xi = x+dx
        yi = y+dy
        if 0 <= xi < 12 and 0 <= yi < 6:
            if [xi,yi] not in ls:
                if bd[xi][yi] == clr:
                    ls.append([xi,yi])
                    go_puyo(xi,yi,clr)


bd = [list(input()) for i in range(12)]
bomb = 0
while True:
    flag = 0
    go_down()
    for x in range(12):
        for y in range(6):
            if bd[x][y] != '.':
                ls = []
                go_puyo(x,y,bd[x][y])
                if len(ls) >= 4:
                    for x, y in ls:
                        bd[x][y] = '.'
                        flag = 1
    if flag == 1:
        bomb += 1
    else :
        break
print(bomb)
