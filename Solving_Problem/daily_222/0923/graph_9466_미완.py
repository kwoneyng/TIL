def dfs(i,end,nxt,ls=[]):
    if nxt[i] == end:
        if nxt[i] not in rs:
            rs.append(nxt[i])
        rs.extend(ls)
        return 0
    else:
        if nxt[i] not in ls:
            dfs(nxt[i],end,nxt,ls+[nxt[i]])


for t in range(int(input())):
    n=int(input())
    rs=[]
    nxt=[0]+list(map(int,input().split()))
    vis=[[] for i in range(n+1)]
    for i in range(1,n+1):
        if i not in rs:
            dfs(i,i,nxt)
    print(n-len(rs))