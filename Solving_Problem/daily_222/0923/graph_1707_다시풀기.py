def dfs(now, group, a, chk):
    chk[now] = group
    for i in nxt_ls[now]:
        if chk[i] == 0:
            if dfs(i, -group, a, chk) is False:
                return False
        elif chk[i] == chk[now]:
            return False
    return True


for t in range(int(input())):
    v, e = list(map(int, input().split()))
    nxt_ls = [[] for i in range(v+1)]
    chk = [0]*(v+1)
    su_set = []
    for i in range(e):
        st,ed = list(map(int,input().split()))
        nxt_ls[st].append(ed)
        nxt_ls[ed].append(st)
    ans = True
    for i in range(1,v+1):
        if chk[i] == 0:
            if dfs(i, 1, nxt_ls, chk) is False :
                ans = False
                break
    if ans :
        print('YES')
    else: 
        print('NO')

