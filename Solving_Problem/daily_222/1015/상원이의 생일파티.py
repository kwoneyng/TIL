for t in range(int(input())):
    n,m = map(int, input().split())
    nxt_ls = [[] for i in range(n+1)]
    vis = [0]*(n+1)
    for i in range(m):
        a,b = map(int, input().split())
        nxt_ls[a].append(b)
        nxt_ls[b].append(a)
    q = [(1,0)]
    vis[1] = 1
    cnt = 0
    while q:
        st,key = q.pop(0)
        for j in nxt_ls[st]:
            if vis[j] == 0 and key <= 1:
                cnt += 1
                vis[j] = 1
                q.append((j,key+1))
    print('#{}'.format(t+1),cnt)
