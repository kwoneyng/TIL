from collections import deque

def higher(i):
    vis = [0]*(n+1)
    q = deque()
    q.append(i)
    cnt = 0
    while q:
        c = q.popleft()
        if vis[c] == 0:
            vis[c] = 1
            cnt += 1
            for k in high[c]:
                q.append(k)
    return cnt


def lower(i):
    vis = [0]*(n+1)
    q = deque()
    q.append(i)
    cnt = 0
    while q:
        c = q.popleft()
        if vis[c] == 0:
            vis[c] = 1
            cnt += 1
            for k in low[c]:
                q.append(k)
    return cnt

for t in range(1,int(input())+1):
    n,m = int(input()), int(input())
    high = [[] for i in range(n+1)]
    low = [[] for i in range(n+1)]
    rs = 0
    for i in range(m):
        a,b = map(int,input().split())
        high[a].append(b)
        low[b].append(a)
    for i in range(1,n+1):
        if higher(i) + lower(i) == n+1:
            rs += 1
        
    print(f'#{t} {rs}')
