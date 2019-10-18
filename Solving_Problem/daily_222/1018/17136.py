def perm(ls=[]):
    if len(ls) == k:
        perm_set.append(ls)
        return
    for i in range(k):
        if i not in ls:
            perm(ls+[i])

def rotate(r,c,s,bd):
    for i in range(s,0,-1):
        temp = bd[r-i][c-i]
        for y in range(c-i,c+i):
            temp, bd[r-i][y+1] = bd[r-i][y+1], temp
        for x in range(r-i,r+i):
            temp, bd[x+1][c+i] = bd[x+1][c+i],temp
        for y in range(c+i,c-i,-1):
            temp, bd[r+i][y-1] = bd[r+i][y-1], temp
        for x in range(r+i,r-i,-1):
            temp, bd[x-1][c-i] = bd[x-1][c-i], temp


from collections import deque
n,m,k = map(int,input().split())
obd = deque([[0]*(m+1)])
for i in range(n):
    obd.append([0]+list(map(int,input().split())))
data = deque()
mn = 99999
perm_set = deque()
perm()
for i in range(k):
    data.append(list(map(int,input().split())))

for i in perm_set:
    bd=[i[:] for i in obd]
    for j in i: 
        r,c,s = data[j]
        rotate(r,c,s,bd)
        for k in bd[1:]:
            rs = sum(k)
            if rs < mn:
                mn = rs
print(mn)

