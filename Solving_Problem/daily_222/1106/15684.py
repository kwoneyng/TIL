def go(su,ls=[],idx=0):
    global rs
    if len(ls) == su:
        for i in ls:
            x,y = ht[i]
            bd[x][y] = 1
        for i in range(n):
            x,y = 0,i
            while x < h:
                if bd[x][y] == 1:
                    y+=1
                elif bd[x][y-1] == 1 and y > 0:
                    y-=1
                x+=1
            if y != i:
                for i in ls:
                    x,y = ht[i]
                    bd[x][y] = 0
                return
        rs = len(ls)
        return

    for k in range(idx,cnt):
        go(su,ls+[k],k+1)
        if rs != -1:
            return


n,m,h = map(int,input().split())
bd = [[0]*n for i in range(h)]
ht = {}
for i in range(m):
    x,y = map(int, input().split())
    x-=1
    y-=1
    bd[x][y] = 1
cnt = 0
for x in range(h):
    for y in range(n-1):
        if bd[x][y] == 0:
            ht[cnt] = x,y
            cnt += 1
rs = -1
for i in range(4):
    go(i)
    if rs != -1:
        break
print(rs)