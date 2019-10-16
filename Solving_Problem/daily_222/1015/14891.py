def match(ls):
    rs = [0]*3
    for i in range(3):
        if ls[i][2] != ls[i+1][6]:
            rs[i] = 1
    return rs

def nearR(x,p,i=0,vis=[]):
    if 0 <= x+i < 3:
        if x+i not in vis:
            if mat[x+i] == 1:
                if p == 1:
                    top[x+i+1].append(top[x+i+1].pop(0))
                else:
                    top[x+i+1].insert(0,top[x+i+1].pop())
                nearR(x,-p,i+1,vis+[x+i])
def nearL(x,p,i=0,vis=[]):
    if 0 <= x-1-i:
        if x-1-i not in vis:
            if mat[x-1-i] == 1:
                if p == 1:
                    top[x-1-i].append(top[x-1-i].pop(0))
                else:
                    top[x-1-i].insert(0,top[x-1-i].pop())
                nearL(x,-p,i+1,vis+[x-i])
top = []
for i in range(4):
    top.append(list(map(int,input())))

k = int(input())
for _ in range(k):
    mat = match(top)
    i, p = map(int,input().split())
    i -= 1
    if p == -1:
        top[i].append(top[i].pop(0))
    else:
        top[i].insert(0,top[i].pop())
    nearR(i,p)
    nearL(i,p)
rs = 0
for i in range(4):
    if top[i][0] == 1:
        rs += 2**i

print(rs)
    