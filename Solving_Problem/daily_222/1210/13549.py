from collections import deque

def go():
    if n == m:
        print(0)
        return
    q = deque([n])
    vis = [0] * 100001
    vis[n] = 1
    cnt = 0
    while q:
        for i in range(len(q)):
            nxt = q[i]
            while 0 < nxt*2 < 100001 and nxt*2 < m*2:
                nxt *= 2
                if nxt == m:
                    print(cnt)
                    return
                vis[nxt] = 1
                q.append(nxt)
        cnt += 1
        for i in range(len(q)):
            nxt = q.popleft()
            for nnxt in [nxt-1, nxt+1]:
                if 0 <= nnxt < 100001:
                    if nnxt == m:
                        print(cnt)
                        return
                    if vis[nnxt] == 0:
                        vis[nnxt] = 1
                        q.append(nnxt)


n,m = map(int,input().split())
go()