from collections import deque

for t in range(int(input())):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    nxt_ls = [[] for i in range(n+1)]
    vis = [0]*(n+1)
    q = deque()
    cnt = 1
    for i in range(m):
        nxt_ls[data[2*i]].append(data[2*i+1])
        nxt_ls[data[2*i+1]].append(data[2*i])
    for i in range(1,n+1):
        if vis[i] == 0:
            q.append(i)
        else:
            continue
        while q:
            no = q.popleft()
            vis[no] = 1
            for j in nxt_ls[no]:
                if vis[j] == 0:
                    q.append(j)
        if sum(vis) == n:
            break
        else:
            cnt += 1
    print('#{}'.format(t+1),cnt)