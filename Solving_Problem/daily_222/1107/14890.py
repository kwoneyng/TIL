def down(x,y,bd):
    global path
    root = bd[x][y]
    cnt = 1
    while x < n-1:
        x += 1
        if root == bd[x][y]:
            cnt += 1
        elif root == bd[x][y]+1:
            for i in range(l):
                if x+i > n-1:
                    return
                if bd[x+i][y] != bd[x][y]:
                    return
            root -= 1
            x += l-1
            cnt = 0
        elif root+1 == bd[x][y]:
            if cnt >= l:
                root += 1
                cnt = 1
            else:
                return
        else:
            return
    # print(f'down {y}')
    path += 1            
        


def right(x,y,bd):
    global path
    root = bd[x][y]
    cnt = 1
    while y < n-1:
        y += 1
        if root == bd[x][y]:
            cnt += 1
        elif root == bd[x][y]+1:
            for i in range(l):
                if y+i > n-1:
                    return
                if bd[x][y+i] != bd[x][y]:
                    return
            root -= 1
            y += l-1
            cnt = 0
        elif root+1 == bd[x][y]:
            if cnt >= l:
                root += 1
                cnt = 1
            else:
                return
        else:
            return
    # print(f'right {x}')
    path += 1            


n,l = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(n)]
path = 0
for i in range(n):
    down(0,i,bd)
    right(i,0,bd)
print(path)