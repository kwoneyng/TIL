n, m = map(int, input().split())
gp = [[] for i in range(n+1)]
vis = [0]*(n+1)
for i in range(m):
    j, k = map(int, input().split())
    gp[j].append(k)
    gp[k].append(j)
cnt = 0
for i in range(1, n+1):
    if vis[i]:
        continue
    cnt += 1
    stack = []
    stack.extend(gp[i])
    while stack:
        chk = stack.pop()
        vis[chk] = 1
        for i in gp[chk]:
            if not vis[i]:
                stack.append(i)
print(cnt)