def bcg(x,y,leng):
    global cnt, paper
    if cnt[leng] == 0:
        return 0
    for a in range(x,x+leng):
        for b in range(y,y+leng):
            if bd[a][b] == 0:
                return 0
    for a in range(x,x+leng):
        for b in range(y,y+leng):
            bd[a][b] = 0
            paper -= 1
    cnt[leng] -= 1
    return 1

def go(sx,sy,obd):
    bd = [i[:] for i in obd]
    for i in range(5):
        if bcg(sx,sy,i) == 1:
            for x in range(sx,10):
                for y in range(10):
                    if bd[x][y] == 1:
                        go(x,y,bd)
            


bd=[list(map(int, input().split())) for i in range(10)]
cnt = [5]*5
paper = 0
sx,sy = -1, -1
for x in range(10):
    for y in range(10):
        if bd[x][y] == 1:
            if sx == -1:
                sx,sy = x,y
            paper += 1

go(sx,sy,bd)
