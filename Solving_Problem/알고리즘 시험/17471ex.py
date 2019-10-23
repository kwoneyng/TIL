def perm(x, y, xls=[], yls=[]):
    global n
    if len(xls) == x and len(yls) == y:
        xls.sort()
        yls.sort()
        if [xls,yls] not in rs_set:
            rs_set.append([xls,yls])
        return 0

    if len(xls) == 0:
        for i in range(1,n+1):
            perm(x,y,xls+[i],yls)
    elif len(xls) < x:
        for i in range(1,n+1):
            if i not in xls:
                perm(x,y,xls+[i],yls)
    elif len(yls) == 0:
        for i in range(1,n+1):
            if i not in xls:
                perm(x,y,xls,yls+[i])
    elif len(yls) < y:
        for i in range(1,n+1):
            if i not in xls and i not in yls:
                perm(x,y,xls,yls+[i])

def check(xls, yls):
    xset = set()
    yset = set()
    rs = 0
    for i in xls:
        for j in nxt_ls[i]:
            xset.add(j)
    for i in yls:
        for j in nxt_ls[i]:
            yset.add(j)
    if len(xls) > 1:
        for i in xls:
            if i not in xset:
                return 0
    if len(yls) > 1:
        for i in yls:
            if i not in yset:
                return 0
    for i in xls:
        rs += su[i]
    for i in yls:
        rs -= su[i]
    rss_st.append(abs(rs))
    return 0


n = int(input())
su = list(map(int, input().split()))
su.insert(0,0)
nxt_ls = [[] for i in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    nx = data.pop(0)
    for j in data:
        nxt_ls[i].append(j)
su_set = []
rs_set = []
rss_st = []
for i in range(1,n//2+1):
    su_set.append([i,n-i])
for x,y in su_set:
    perm(x,y)
for xls, yls in rs_set:
    check(xls,yls)
if rss_st:
    print(min(rss_st))
else :
    print(-1)

