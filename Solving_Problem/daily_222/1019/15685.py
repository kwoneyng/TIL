rec = [[0,1],[1,0],[1,1]]
def dragon(dd,ls,dc,g=1):
    if g == 11:
        return
    x,y = ls[-1]
    for i in range(len(ls)-2,-1,-1):
        a,b = ls[i]
        dx,dy = x-a,y-b
        dx,dy = -dy,dx
        c,d = x+dx,y+dy
        ls.append([c,d])
    dc[dd][g].extend(ls)
    dragon(dd,ls,dc,g+1)


n=int(input())
data = []
bd=[[0]*101 for i in range(101)]
for i in range(n):
    data.append(list(map(int,input().split())))
dc = [[[] for i in range(11)] for i in range(4)]
ls = [[0,0]]
for i in range(4):
    if i == 0:
        ls.append([0,1])
        dc[i][0].extend(ls)
        dragon(i,ls,dc)
        ls = [[0,0]]
    elif i == 1:
        ls.append([-1,0])
        dc[i][0].extend(ls)
        dragon(i,ls,dc)
        ls = [[0,0]]
    elif i == 2:
        ls.append([0,-1])
        dc[i][0].extend(ls)
        dragon(i,ls,dc)
        ls = [[0,0]]
    elif i == 3:
        ls.append([1,0])
        dc[i][0].extend(ls)
        dragon(i,ls,dc)

for i in data:
    y,x,d,g = i
    for a,b in dc[d][g]:
        bd[x+a][y+b] = 1
rs = 0
for x in range(100):
    for y in range(100):
        if bd[x][y] == 1:
            flag = 1
            for a,b in rec:
                xi,yi = x+a,y+b
                if bd[xi][yi] != 1:
                    flag = 0
                    break
            if flag == 1:
                rs += 1
print(rs)
# for i in bd:
#     print(i)
