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
            if onepan[i][j] != 0:
                su += 1
                total += onepan[i][j]
            if j+1 < m:
                if onepan[i][j] == onepan[i][j+1] and onepan[i][j] != 0:
                    flag = 1
                    if vis[i][j] == 0:
                        vis[i][j] = 1
                        ls.append([i,j])
                    if vis[i][j+1] == 0:
                        vis[i][j+1] = 1
                        ls.append([i,j+1])
            if i+1 < n+1:
                if onepan[i][j] == onepan[i+1][j] and onepan[i][j] != 0:
                    flag = 1
                    if vis[i][j] == 0:
                        vis[i][j] = 1
                        ls.append([i,j])
                    if vis[i+1][j] == 0:
                        vis[i+1][j] = 1
                        ls.append([i+1,j])                        
        if onepan[i][0] == onepan[i][m-1] and onepan[i][0] != 0:
            flag = 1
            if vis[i][0] == 0:
                vis[i][j] = 1
                ls.append([i,0])
            if vis[i][m-1] == 0:
                vis[i][m-1] = 1
                ls.append([i,m-1])
    for i,j in ls:
        onepan[i][j] = 0
                

n,m,t = map(int,input().split())
onepan = [[] for i in range(n+1)]
data = []
for i in range(n):
    onepan[i+1].extend(list(map(int,input().split())))
for i in range(t):
    data.append(list(map(int, input().split())))

for x,d,k in data:
    flag = 0
    su = 0
    total = 0
    vis = [[0]*(m) for i in range(n+1)]
    rotate(x,d,k)
    find()
    if flag == 0:
        cut = total/su
        for i in range(1,n+1):
            for j in range(m):
                if 0 < onepan[i][j] < cut:
                    onepan[i][j] += 1
                elif cut < onepan[i][j]:
                    onepan[i][j] -= 1 
frs = 0
for i in onepan[1:]:
    frs += sum(i)
print(frs)
