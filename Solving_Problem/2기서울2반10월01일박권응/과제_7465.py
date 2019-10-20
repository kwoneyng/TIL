def vis_chk():
    if vis.count(0) != 0:
        return False
    else:
        return True

def friend(start=1, su=1):
    q = [start]
    while q:
        nxt = q.pop(0)
        if vis[nxt] == 0:
            vis[nxt] = su
            q.extend(rel[nxt])
    if vis_chk():
        return
    else:
        for i in range(len(vis)):
            if vis[i] == 0:
                friend(i,su+1)
                break

        
for t in range(int(input())):
    n,m = map(int, input().split())
    rel = [[] for i in range(n+1)]
    vis = [1]+[0]*(n)
    for i in range(m):
        a,b = map(int,input().split())
        rel[a].append(b)
        rel[b].append(a)
    friend()
    print('#{}'.format(t+1),max(vis))