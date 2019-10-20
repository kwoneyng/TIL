# 연결된거 찾기

def perm(x,ls=[],st=1):
    global n
    if len(ls) == x:
        anls = []
        for i in sls:
            if i not in ls:
                anls.append(i)
        rs_set.append([ls,anls])
        return 0
    for i in range(st,n+1):
        perm(x,ls+[i],i+1)

def check(ls):
    if len(ls) == 1:
        return True
    else:
        for st in range(len(ls)-1):
            for ed in range(st+1,len(ls)):
                if go(ls[st],ls[ed]) != 1:
                    return False
        return True    

def go(st, ed, vis=[]):
    if st == ed:
        return 1
    for i in nxt_ls[st]:
        if i not in vis:
            if go(i,ed,vis+[i]) == 1:
                return 1


n = int(input())
sls = [i for i in range(1,n+1)]
su = [0] + list(map(int, input().split()))
nxt_ls = [[] for i in range(n+1)]
for i in range(1,n+1):
    data = list(map(int, input().split()))
    nxt_ls[i].extend(data[1:])
su_set = []
rs_set = []
rs_fin = []
for i in range(1,n//2+1):
    perm(i)
for x,y in rs_set:
    rs = 0
    if check(x) and check(y):
        for i in x:
            rs += i
        for i in y:
            rs -= i
        if abs(rs) == 1:
            print(x, y)
        rs_fin.append(abs(rs))
print(rs_fin)
if rs_fin:
    print(min(rs_fin))
else:
    print(-1)