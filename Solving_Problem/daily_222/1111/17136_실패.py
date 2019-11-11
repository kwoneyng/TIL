def one(x,y,temp,use):
    global min_use, chk
    if paper[0] == 0:
        return
    temp[x][y] = 0
    use += 1
    paper[0] -= 1
    chk -= 1
    if chk == 0:
        min_use = min(use,min_use)

    search(temp,x,use)
    use -= 1
    temp[x][y] = 1
    paper[0] += 1
    chk += 1

def two(x,y,temp,use):
    global min_use, chk
    if paper[1] == 0:
        return
    for i in range(x,x+2):
        for j in range(y,y+2):
            if i >= 10 or j >= 10 or temp[i][j] == 0:
                return
    for i in range(x,x+2):
        for j in range(y,y+2):
            temp[i][j] = 0
            chk -= 1
    use += 1
    paper[1] -= 1
    if chk == 0:
        min_use = min(min_use,use)

    search(temp,x,use)
    use -= 1
    paper[1] += 1
    for i in range(x,x+2):
        for j in range(y,y+2):
            temp[i][j] = 1
            chk += 1
    

def thr(x,y,temp,use):
    global chk, min_use
    if paper[2] == 0:
        return
    for i in range(x,x+3):
        for j in range(y,y+3):
            if i >= 10 or j >= 10 or temp[i][j] == 0:
                return
    for i in range(x,x+3):
        for j in range(y,y+3):
            temp[i][j] = 0
            chk -= 1
    use += 1
    paper[2] -= 1
    if chk == 0:
        min_use = min(min_use,use)
    search(temp,x,use)
    use -= 1
    paper[2] += 1
    for i in range(x,x+3):
        for j in range(y,y+3):
            temp[i][j] = 1
            chk += 1

def four(x,y,temp,use):
    global chk, min_use
    if paper[3] == 0:
        return
    for i in range(x,x+4):
        for j in range(y,y+4):
            if i >= 10 or j >= 10 or temp[i][j] == 0:
                return
    for i in range(x,x+4):
        for j in range(y,y+4):
            temp[i][j] = 0
            chk -= 1
    use += 1
    paper[3] -= 1
    if chk == 0:
        min_use = min(min_use, use)
    search(temp,x,use)
    use -= 1
    paper[3] += 1
    for i in range(x,x+4):
        for j in range(y,y+4):
            temp[i][j] = 1
            chk += 1

def five(x,y,temp,use):
    global chk, min_use
    if paper[4] == 0:
        return
    for i in range(x,x+5):
        for j in range(y,y+5):
            if i >= 10 or j >= 10 or temp[i][j] == 0:
                return
    for i in range(x,x+5):
        for j in range(y,y+5):
            temp[i][j] = 0
            chk -= 1
    use += 1
    paper[4] -= 1
    if chk == 0:
        min_use = min(min_use,use)
    search(temp,x,use)
    use -= 1
    paper[4] += 1
    for i in range(x,x+5):
        for j in range(y,y+5):
            temp[i][j] = 1
            chk += 1

func = [five,four,thr,two,one]

def search(bd,sx=0,use=0):
    global min_use
    if chk == 0:
        min_use = min(use,min_use)
    temp = bd
    for x in range(sx,10):
        for y in range(10):
            if temp[x][y] == 1:
                for i in range(5):
                    func[i](x,y,temp,use)

bd = [list(map(int,input().split())) for i in range(10)]
paper = [5,5,5,5,5]
min_use = 26
chk = 0
for x in range(10):
    for y in range(10):
        if bd[x][y] == 1:
            chk += 1
search(bd)
if min_use < 26:
    print(min_use)
else :
    print(-1)