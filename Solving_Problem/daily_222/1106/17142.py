from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def comb(i=0,ls=[]):
    if len(ls) == m:
        comb_set.append(ls)
        return
    for _ in range(i,virus):
        comb(_+1,ls+[_])

def spread(q,temp,bd):
    global mn
    cnt = 0
    while q:
        if temp == 0:
            mn = min(mn,cnt)
            return
        if mn < cnt:
            return
        cnt += 1
        for i in range(len(q)):
            x,y = q.popleft()
            for j in range(4):
                a,b = dx[j],dy[j]
                xi,yi = a+x,b+y
                if 0 <= xi < n and 0 <= yi < n:
                    if bd[xi][yi] == 0:
                        bd[xi][yi] = 1
                        temp -= 1
                        q.append([xi,yi])
                    elif bd[xi][yi] == 2:
                        bd[xi][yi] = 1
                        q.append([xi,yi])


n,m = map(int, input().split())
obd = [list(map(int,input().split())) for i in range(n)]
k = 0
ht = {}
comb_set = deque()
mn = 9999999999999999999999999999
virus = 0
for x in range(n):
    for y in range(n):
        if obd[x][y] == 2:
            ht[virus] = x,y
            virus += 1
        elif obd[x][y] == 0:
            k += 1
# print(ht)
if k == 0:
    print(0)
else :
    comb()
    for i in comb_set:
        q = deque()
        bd = [j[:] for j in obd]
        temp = k
        for _ in i:
            x,y = ht[_]
            q.append([x,y])
        spread(q,temp,bd)
    if mn > 999999999999999999999:
        print(-1)
    else:
        print(mn)
