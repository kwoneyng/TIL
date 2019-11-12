def attach(x,y,i):
    global chk
    if paper[i-1] :
        for l in range(x,x+i):
            for m in range(y,y+i):
                if l > 9 or m > 9 or bd[l][m] == 0:
                    return
        for l in range(x,x+i):
            for m in range(y,y+i):
                bd[l][m] = 0
                chk -= 1
        paper[i-1] -= 1
        return 1

def find(sx):
    for x in range(sx,10):
        for y in range(10):
            if bd[x][y] == 1:
                return x,y

def detach(x,y,i):
    global chk
    for l in range(x,x+i):
        for m in range(y,y+i):
            bd[l][m] = 1
            chk += 1
    paper[i-1] += 1

def search(bd,sx=0, use=0):
    global min_use
    if chk == 0:
        min_use = use
        return
    if min_use <= use:
        return
    x,y = find(sx)
    for i in range(5,0,-1):
        if attach(x,y,i) == 1:
            search(bd,x,use+1)
            detach(x,y,i)



bd = [list(map(int,input().split())) for i in range(10)]
paper = [5,5,5,5,5]
min_use = 9999
chk = 0
for x in range(10):
    for y in range(10):
        if bd[x][y] == 1:
            chk += 1

search(bd)
if min_use > 99:
    print(-1)
else:
    print(min_use)