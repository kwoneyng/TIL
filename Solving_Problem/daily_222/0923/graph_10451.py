def dfs(i,cnt,nxt,vis):
    if vis[i] == 0:
        vis[i] = cnt
        dfs(nxt[i],cnt,nxt,vis)



for t in range(int(input())):
    n = int(input())
    nxt = [0]+list(map(int,input().split()))
    vis = [0]*(n+1)
    cnt = 1
    for i in range(1, n+1):
        if vis[i] == 0:
            dfs(i,cnt,nxt,vis)
            cnt += 1
    print(max(vis))