from pprint import pprint

def play(i, xyd):
    global h, w
    x, y, d = xyd
    if i == 'U':
        j = 0
        dx, dy = di[j]

    elif i == 'R':
        j = 1
        dx, dy = di[j]
    
    elif i == 'D':
        j = 2
        dx, dy = di[j]
    
    elif i == 'L':
        j = 3
        dx, dy = di[j]

    elif i == 'S':
        dx, dy = 0, 0
        j = d
        shoot(xyd)

    X = x+dx
    Y = y+dy
    if 0 <= X < h and 0 <= Y < w:
        if bd[X][Y] == '.':
            bd[x][y] = '.'
            bd[X][Y] = d_mark[j]
            q.append([X, Y, j])
        else :
            bd[x][y] = d_mark[j]
            q.append([x, y, j])
    else:
        bd[x][y] = d_mark[j]
        q.append([x,y,j])
                
def shoot(xyd):
    global h, w
    x, y, d = xyd
    dx, dy = di[d]
    X = x+dx
    Y = y+dy
    while True :
        if 0 <= X < h and 0 <= Y < w:
            if bd[X][Y] == '*':
                bd[X][Y] = '.'
                break
            elif bd[X][Y] == '#':
                break
        else :
            break
        X += dx
        Y += dy


for T in range(int(input())):
    h, w = map(int, input().split())
    bd = [list(input()) for i in range(h)]
    n = int(input())
    cm_set = list(input())
    q = []
    di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d_mark = ['^', '>', 'v', '<']
    for x in range(h):
        for y in range(w):
            if bd[x][y] == '^':
                q.append([x,y,0])
            elif bd[x][y] == '>':
                q.append([x,y,1])
            elif bd[x][y] == 'v':
                q.append([x,y,2])
            elif bd[x][y] == '<':
                q.append([x,y,3])
    for i in cm_set:
        play(i, q.pop(0))
    
    print('#{} '.format(T+1), end='')
    for x in bd:
        print(''.join(x))
