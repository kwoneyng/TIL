def solve(s=0,ls=[]):
    if ls and len(ls) < n:
        for i in range(n):
            vis[i] = 0
        mark(ls)
    for i in range(s,n):
        ls.append(i)
        solve(i+1,ls)
        ls.pop()

def mark(ls):
    global mn
    for i in ls:
        vis[i] = 1
    q = []
    q.append(i)
    vis[i] = 2
    rs1 = 0
    rs2 = 0
    while q:
        point = q.pop(0)
        rs1 += su[point]
        for i in nxt_ls[point]:
            if vis[i] == 0:
                continue
            elif vis[i] == 1:
                q.append(i)
                vis[i] = 2 
    if vis.count(1):
        return
    i = vis.index(0)
    vis[i] = -1
    q.append(i)
    while q:
        point = q.pop(0)
        rs2 += su[point]
        for i in nxt_ls[point]:
            if vis[i] != 0:
                continue
            elif vis[i] == 0:
                q.append(i)
                vis[i] = -1
    if vis.count(0):
        return
    # if mn > abs(rs1-rs2):
    #     print(ls, rs1, rs2)
    mn = min(mn,abs(rs1-rs2))
    

n = int(input())
su = list(map(int,input().split()))
nxt_ls = [[] for i in range(n)]
vis = [0]*(n)
mn = 99999999999999999999999999999
for i in range(n):
    data = list(map(int,input().split()))
    t = data.pop(0)
    for _ in range(t):
        nxt_ls[i].append(data.pop(0)-1)
solve()
if mn > 9999999999999:
    print(-1)
else:
    print(mn)