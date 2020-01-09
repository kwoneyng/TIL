from sys import stdin, setrecursionlimit as SRL
input = stdin.readline; SRL(7878781)

n = int(input())
H = list(map(int,input().split()))

R = [1,-1,-1]
L = [2,-1,-1]

depths = {1: [1, 2]}
history = [0]
for h in H:
    if not depths.setdefault(h, []): print(-1); exit()
    x = depths[h].pop()
    history.append(x)
    n = len(R)
    R[x] = n; L[x] = n+1
    R.extend([-1,-1]); L.extend([-1,-1])
    depths.setdefault(h+1, []).extend([n,n+1])

num = [0]*len(R)
def dfs(x, cnt):
    if R[x] == -1: return cnt
    cnt = dfs(L[x], cnt)
    num[x] = str(cnt); cnt+= 1
    cnt = dfs(R[x], cnt)
    return cnt
dfs(0, 1)
print(num)
for x in history: print(num[x], end=' ')