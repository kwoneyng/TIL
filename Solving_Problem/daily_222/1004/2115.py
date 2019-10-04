def perm(i=0,j=0,ls=[]):
    if len(ls) == 2:
        rs.append(ls)
        return

    for x in range(i,n):
        if j+m <= n:
            pass
        else:
            j=0
            continue
        for y in range(j,n):
            if y+m <= n:
                perm(x,y+m,ls+[[x,y]])
            else:
                j = 0
                break

def opti(ls,x=0,rs=0,sel=0,vis=[]):
    global sel_pr, tt
    if tt < sel:
        tt = sel
    for i in range(m):
        if i not in vis:
            if rs+ls[i] <= c:
                opti(ls,i+1,rs+ls[i],sel+ls[i]**2,vis+[i])
            else:
                return


for t in range(int(input())):
    n,m,c = map(int, input().split())
    bd = [list(map(int, input().split())) for i in range(n)]
    rs = []
    pr_set = []
    perm()
    for a,b in rs:
        sel_pr = 0
        tt = 0
        x,y = a
        opti(bd[x][y:y+m])
        sel_pr += tt
        tt = 0
        x,y = b
        opti(bd[x][y:y+m])
        sel_pr += tt
        pr_set.append(sel_pr)
    print('#{}'.format(t+1),end=' ')
    print(max(pr_set))