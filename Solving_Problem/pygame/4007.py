from heapq import heappop, heappush
def rootfind(x):
    q = [[0,x]]
    cnt = n
    while cnt > 0:
        val, node = heappop(q)
        if dpgo[node] == -1:
            dpgo[node] = val
            cnt -= 1
        for nval, nxt in nxtls[node]:
            toval = val+nval
            if dpgo[nxt] == -1:
                heappush(q,[toval,nxt])

def revfind(x):
    q = [[0,x]]
    cnt = n
    while cnt > 0:
        val, node = heappop(q)
        if dpbk[node] == -1:
            dpbk[node] = val
            cnt -= 1
        for nval, nxt in comls[node]:
            toval = val+nval
            if dpbk[nxt] == -1:
                heappush(q,[toval,nxt])

for T in range(int(input())):
    n,m,x = map(int,input().split())
    nxtls = [[] for i in range(n+1)]
    comls = [[] for i in range(n+1)]
    dpgo = [-1]*(n+1)
    dpbk = [-1]*(n+1)
    for i in range(m):
        s,e,t = map(int,input().split())
        nxtls[s].append([t,e])
        comls[e].append([t,s])
    rootfind(x)
    revfind(x)
    dp = [dpgo[i]+dpbk[i] for i in range(1,n+1)]
    print(f'#{T+1} {max(dp)}')
        