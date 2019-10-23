def go(start,td=0,vis=[]):
    global mn
    if td > mn :
        return
    if len(vis) == n:
        x,y = start
        a,b = hm
        dt = abs(x-a)+abs(y-b)
        if mn > td+dt:
            mn = td+dt
            sls.append(vis)
        return

    x,y = start
    for i in range(n):
        if i not in vis:
            a,b = nls[i]
            dt = abs(x-a)+abs(y-b)
            go(nls[i],td+dt,vis+[i])


for t in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    nls = []
    mn = 99999999999999999999999999
    sls = []
    for i in range(n+2):
        ls = []
        for j in range(2):
            ls.append(data.pop(0))
        nls.append(ls)
    cp = nls.pop(0)
    hm = nls.pop(0)
    go(cp)
    print('#{}'.format(t+1),mn)