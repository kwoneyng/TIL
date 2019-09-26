def perm(x,ls=[],st=1):
    global n
    if len(ls) == x:
        als=[]
        for i in sls:
            if i not in ls:
                als.append(i)
        su_set.append([ls,als])
    for i in range(st,n+1):
        perm(x,ls+[i],i+1)


def dfs(x,group,nxt,vis):
    if vis[x] == group:
        vis[x] = 0
        for i in nxt[x]:
            if dfs(i,group,nxt,vis) == 0:
                return 0
n = int(input())
chk = [0]*(n+1)
sls = [i for i in range(1,n+1)]
su = [0]+list(map(int, input().split()))
nxt_ls = [[] for i in range(n+1)]
su_set=[]
rs_set=[]
for i in range(1, n+1):
    nxt_ls[i].extend(list(map(int,input().split()))[1:])
for i in range(1,n//2+1):
    perm(i)
for x,y in su_set:
    vis=[0]*(n+1)
    for i in x:
        vis[i] = 1
    a = i
    for i in y:
        vis[i] = 2
    b = i
    dfs(a,1,nxt_ls,vis)
    dfs(b,2,nxt_ls,vis)
    if vis == chk:
        rs = 0
        for i in x:
            rs += su[i]
        for i in y:
            rs -= su[i]
        rs_set.append(abs(rs))
if rs_set:
    print(min(rs_set))
else:
    print(-1)