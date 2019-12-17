near = [[-1,0], [0,1], [1,0], [0,-1]]
def sellect(st, ls=[], rs=0):
    if rs > 3:
        return
    if len(ls) == 7:
        perm.append(ls)
        return
    for i in range(st, 25):
        sellect(i+1,ls+[i],rs+bd[ht[i][0]][ht[i][1]])


def check():
    global rs
    for i in perm:
        q = [i[0]]
        vis = [[0]*5 for i in range(5)]
        count = 0
        while q:
            idx = q.pop(0)
            x,y = ht[idx]
            if vis[x][y] == 0:
                vis[x][y] = 1
                count += 1
            for a,b in near:
                xi, yi = a+x, b+y
                if 0 <= xi < 5 and 0 <= yi < 5:
                    if vis[xi][yi] == 0:
                        nidx = rht[(xi,yi)]
                        if nidx in i:
                            q.append(nidx)
        if count == 7:
            rs += 1


bd = []
for i in range(5):
    data = list(input())
    ls = []
    for j in data:
        if j == 'S':
            ls.append(0)
        else:
            ls.append(1)
    bd.append(ls)

cnt = 0
ht = {}
rht = {}
rs = []
start = [-1,-1]
perm = []
rs = 0
for x in range(5):
    for y in range(5):
        if bd[x][y] == 0 and start == [-1,-1]:
            start = (x,y)
        ht[cnt] = (x,y)
        rht[(x,y)] = cnt
        cnt += 1

sellect(rht[start])
check()
print(rs)