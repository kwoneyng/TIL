import sys
sys.setrecursionlimit(9999)
def select(ls=[],s=0,mn=0,mx=0):
    global rs
    if rs > 0:
        return
    if mn > e:
        return
    if n-s+len(ls) < p:
        return
    if len(ls) == p:
        make_su(ls,mn,mx)
        rs = 1
        return
    for i in range(s,n):
        select(ls+[i],s+1,mn+data[i][0],mx+data[i][1])
        select(ls,s+1,mn,mx)


def combination(now_idx, left, right, arr, length):
    global result
    if length == P:
        if left <= E <= right:
            mn, mx = 0,0
            for x,y in arr:
                mn+=x
                mx+=y
            make_su(arr,mn,mx)
            return 
        return
    if left >= E or (N - now_idx < P - length):
        return 
    for nxt in range(now_idx + 1, N):
        combination(nxt, left + data[0][nxt], right + data[1][nxt], arr + [nxt], length + 1)
        if result != -1:
            return


def make_su(ls,mn,mx):
    stdd = mn
    while True:
        for i in ls:
            x, y = data[i]
            if x < y:
                dt = (y+x)//2 - x
                stdd += dt
                if stdd > e:
                    stdd -= dt
                    data[i] = x, y-dt-1
                else:
                    data[i] = x+dt, y
            if stdd == e:
                rs = ['0']*n
                for i in ls:
                    rs[i] = str(data[i][0])
                print(' '.join(rs))
                return



n,p,e = map(int,input().split())
rs = -1
data = []
for i in range(n):
    x,y = list(map(int,input().split()))
    data.append([x,y])
select()
if rs == -1:
    print(-1)