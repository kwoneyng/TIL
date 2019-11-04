n = int(input())
k = int(input())
bd = [[0]*n for i in range(n)]
bd[0][0] = 2
pal = [0,1]
for i in range(k):
    x,y = map(int,input().split())
    x-=1
    y-=1
    bd[x][y] = 1
l = int(input())
data = {}
for i in range(l):
    a,b = list(input().split())
    data[int(a)] = b
bam = [[0,0]]
x,y = 0,0
t = 0
while True:
    if data.get(t):
        if data[t] == 'D':
            dx,dy = pal
            dx,dy = dy, -dx
            pal = [dx,dy]
        elif data[t] == 'L':
            dx,dy = pal
            dx,dy = -dy, dx
            pal = [dx,dy]
    dx,dy = pal
    x+=dx
    y+=dy
    if 0 <= x < n and 0 <= y <n :
        if bd[x][y] == 1:
            bam.append([x,y])
            bd[x][y] = 2
        elif bd[x][y] == 2:
            print(t+1)
            break
        elif bd[x][y] == 0:
            bam.append([x,y])
            a,b = bam.pop(0)
            bd[a][b] = 0
            bd[x][y] = 2
    else :
        print(t+1)
        break
    t += 1
