near=[[-1,0],[0,1],[1,0],[0,-1]]
def rotate(x,d,k):
    for i in range(1,n+1):
        if i%x == 0:
            if d == 0:
                for _ in range(k):
                    onepan[i][0:0]=[onepan[i].pop()]
            else :
                for _ in range(k):
                    onepan[i].append(onepan[i].pop(0))

def find():
    global flag,su,total
    ls = []
    for i in range(1,n+1):
        for j in range(m):
            if onepan[i][j] > 0:
                total += onepan[i][j]
                su += 1
            for a,b in near:
                xi,yi = i+a,j+b
                if 0 < xi < n+1 and 0 <= yi < m:
                    if onepan[xi][yi] == onepan[i][j] and onepan[i][j] > 0:
                        if [i,j] not in ls:
                            ls.append([i,j])
                        if [xi,yi] not in ls:
                            ls.append([xi,yi])
        if onepan[i][0] == onepan[i][m-1] and onepan[i][0] > 0:
            if [i,0] not in ls:
                ls.append([i,0])
            if [i,n] not in ls: 
                ls.append([i,m-1])
    for x,y in ls:
        flag = 1
        onepan[x][y] = 0

                

n,m,t = map(int,input().split())
onepan = [[] for i in range(n+1)]
data = []
for i in range(n):
    onepan[i+1].extend(list(map(int,input().split())))
for i in range(t):
    data.append(list(map(int, input().split())))
for x,d,k in data:
    total = 0
    su = 0
    flag = 0
    rotate(x,d,k)
    find()
    if flag == 0:
        if su == 0:
            break
        mid = total/su
        for i in range(1,n+1):
            for j in range(m):
                if 0 < onepan[i][j] <= mid:
                    onepan[i][j] += 1
                elif onepan[i][j] > mid :
                    onepan[i][j] -= 1
rs = 0
for i in onepan:
    rs += sum(i)
print(rs)


