from collections import deque
from heapq import heappop, heappush


def rcal():
    global y
    ls = []
    mx = 0
    for i in range(x):
        su = len(bd[i])
        cnt = 0
        for j in range(1,101):
            if bd[i].count(j):
                heappush(ls,[bd[i].count(j),j]) 
                cnt += bd[i].count(j)
            if cnt == su:
                break
        bd[i] = []
        for _ in range(len(ls)):
            many, su = heappop(ls)
            bd[i].append(su)
            bd[i].append(many)
        mx = max(mx, len(bd[i]),y)
    for i in range(x):
        for _ in range(mx-len(bd[i])):
            bd[i].append(0)
    y = mx

def ccal():
    global x
    new = [[] for i in range(y)]
    ls = []
    re_bd = []
    mx = 0
    for i in range(y):
        cnt = 0
        bls =[]
        for j in range(x):
            bls.append(bd[j][i])
        su = len(bls)-bls.count(0)
        for k in range(1,101):
            if bls.count(k):
                heappush(ls,[bls.count(k),k])
                cnt += bls.count(k)
            if cnt == su:
                break
        for _ in range(len(ls)):
            many, su = heappop(ls)
            new[i].append(su)
            new[i].append(many)
        mx = max(mx, len(new[i]),x)
    for i in range(y):
        for _ in range(mx-len(new[i])):
            new[i].append(0)
    x = mx
    for i in range(x):
        ls = []
        for j in range(y):
            ls.append(new[j][i])
        re_bd.append(ls)
    return re_bd
    
    
def debug():
    for i in bd:
        print(i)
    print('-------------------------')

r,c,k = map(int,input().split())
r -= 1
c -= 1
x,y = 3,3
bd = [list(map(int,input().split())) for i in range(x)]

for i in range(101):
    if r < x and c < y:
        if bd[r][c] == k:
            print(i)
            break
    if x >= y:
        rcal()
    else:
        bd = ccal()
        # debug()
else:
    print(-1)