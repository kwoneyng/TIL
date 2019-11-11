near = [[-1,0], [0,1], [1,0], [0,-1]]

def spread():
    new = [[0]*c for i in range(r)]
    for x in range(r):
        for y in range(c):
            if bd[x][y] > 0:
                cnt = 0
                dust = bd[x][y]
                for a,b in near:
                    xi,yi = a+x, y+b
                    if 0 <= xi < r and 0 <= yi < c and bd[xi][yi] != -1:
                        new[xi][yi] += dust//5
                        cnt += 1
                bd[x][y] -= (dust//5)*cnt
    for x in range(r):
        for y in range(c):
            if new[x][y] > 0:
                bd[x][y] += new[x][y]

def blow():
    for i in range(2):
        x,y = cj[i]
        if i == 0:
            clock(x,y)
        else :
            declock(x,y)

def clock(x,y):
    global rs
    temp = 0
    for i in range(y+1,c):
        bd[x][i], temp = temp, bd[x][i]
    for j in range(x-1,-1,-1):
        bd[j][i], temp = temp, bd[j][i]
    for i in range(c-2,-1,-1):
        bd[j][i], temp = temp, bd[j][i]
    for j in range(1,x):
        bd[j][i], temp = temp, bd[j][i]
    rs -= temp

def declock(x,y):
    global rs
    temp = 0
    for i in range(y+1,c):
        bd[x][i], temp = temp, bd[x][i]
    for j in range(x+1,r):
        bd[j][i], temp = temp, bd[j][i]
    for i in range(c-2,-1,-1):
        bd[j][i], temp = temp, bd[j][i]
    for j in range(r-2,x,-1):
        bd[j][i], temp = temp, bd[j][i]
    rs -= temp


r,c,t = map(int,input().split())
bd = [list(map(int,input().split())) for i in range(r)]
cj = []
rs = 0
for x in range(r):
    for y in range(c):
        if bd[x][y] == -1:
            cj.append([x,y])
        elif bd[x][y] > 0 :
            rs += bd[x][y]

for time in range(t):
    spread()
    blow()

print(rs)
# for i in bd:
#     print(i)

