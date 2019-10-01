def f_pal(x,y,pal):
    if pal == 0:
        for a in range(y,m):
            if nbd[x][a] == 6:
                break
            else:
                nbd[x][a] = '#'
    elif pal == 1:
        for a in range(x,n):
            if nbd[a][y] == 6:
                break
            else:
                nbd[a][y] = '#'
    elif pal ==2:
        for a in range(y,-1,-1):
            if nbd[x][a] == 6:
                break
            else:
                nbd[x][a] = '#'
    elif pal == 3:
        for a in range(x,-1,-1):
            if nbd[a][y] == 6:
                break
            else:
                nbd[a][y] = '#'

def chk(pal, camera):
    x,y,no = camera
    if no == 1:
        f_pal(x,y,pal)    
    elif no == 2:
        if pal%2 == 0:
            f_pal(x,y,0)
            f_pal(x,y,2)
        elif pal%2 == 1:
            f_pal(x,y,1)
            f_pal(x,y,3)
    elif no == 3:
        if pal == 0:
            f_pal(x,y,3)
            f_pal(x,y,0)
        elif pal == 1:
            f_pal(x,y,0)
            f_pal(x,y,1)
        elif pal == 2:
            f_pal(x,y,1)
            f_pal(x,y,2)
        elif pal == 3:
            f_pal(x,y,2)
            f_pal(x,y,3)
    elif no == 4:
        for i in range(4):
            if i != pal:
                f_pal(x,y,i)
    elif no == 5:
        for i in range(4):
            f_pal(x,y,i)



def look(ls=[]):
    if len(ls) == ca_su:
        ca_set.append(ls)
        return

    for i in range(4):
        look(ls+[i])


def zero_chk(bd):
    global mn
    rs = 0
    for x in bd:
        rs += x.count(0)
    if mn > rs :
        mn = rs

n,m = map(int, input().split())
bd = [list(map(int, input().split())) for i in range(n)]
mn = 99999999999999999999999999999999
camera = []
for x in range(n):
    for y in range(m):
        if 0 < bd[x][y] < 6:
            camera.append([x,y,bd[x][y]])
ca_su = len(camera)
ca_set = []
look()
for i in ca_set:
    nbd = [i[:] for i in bd]
    for j in range(len(i)):
        chk(i[j],camera[j])
    zero_chk(nbd)
print(mn)