near=[[-1,0],[1,0],[0,-1],[0,1]]
def start(x,y,no,cnt=1):
    global mx, mx_no

    for dx, dy in near:
        xi = x+dx
        yi = y+dy
        if 0 <= xi < n and 0 <= yi < n:
            if bd[x][y] + 1 == bd[xi][yi]:
                start(xi,yi,no,cnt+1)

    if mx < cnt:
        mx = cnt
        mx_no = no
    elif mx == cnt:
        if mx_no > no:
            mx_no = no

for t in range(1,int(input())+1):
    n=int(input())
    bd=[list(map(int,input().split())) for i in range(n)]
    mx = 0
    mx_no=99999999999999999999999999
    for x in range(n):
        for y in range(n):
            start(x,y,bd[x][y])
    print('#{}'.format(t),mx_no, mx)