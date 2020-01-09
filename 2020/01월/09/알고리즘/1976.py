import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
trap = list(map(lambda x:int(x)-1,input().split()))


root = [i for i in range(n)]
def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])

def union(x,y):
    x = find(x)
    y = find(y)

    root[y] = x
rs = 'NO'

def routedef(root):
    global rs
    rt = trap[0]

    for i in range(m-1):
        if find(trap[i]) == find(trap[i+1]):
            continue
        else:
            return
    rs = 'YES'

for x in range(n):
    for y in range(n):
        if bd[x][y] == 1:
            union(x,y)

routedef(root)
print(rs)