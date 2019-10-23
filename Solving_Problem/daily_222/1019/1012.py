import sys
sys.setrecursionlimit(10000)
near = [[-1,0],[0,1],[1,0],[0,-1]]

def jirung(x,y):
    global k
    bd[x][y] = 0
    k -= 1
    for a,b in near:
        xi,yi = x+a,y+b
        if 0 <= xi < n and 0 <= yi < m:
            if bd[xi][yi] == 1:
                jirung(xi,yi)



for t in range(int(input())):
    m,n,k = map(int,input().split())
    bd = [[0]*m for i in range(n)]
    for i in range(k):
        y,x = map(int,input().split())
        bd[x][y] = 1
    cnt = 0
    while True:
        if k == 0:
            break
        flag = 0
        for x in range(n):
            if flag == 1:
                break
            for y in range(m):
                if bd[x][y] == 1:
                    jirung(x,y)
                    flag = 1
                    cnt += 1
                    break
    print(cnt)