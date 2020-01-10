from heapq import heappop, heappush

def go(s,e):
    q = [[0,s]]
    vis = [0]*n
    while q:
        v,x = heappop(q)
        vis[x] = 1
        if x == e:
            return -v
        for nv, nxt in nxt_ls[x]:
            if vis[nxt] == 0:
                if 

n,m = map(int,input().split())

nxt_ls = [[]for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    nxt_ls[a].append([-c,b])
    nxt_ls[b].append([-c,a])
s,e = map(lambda x:int(x)-1,input().split())

print(go(s,e))