near = [[0,1],[1,0]]

def go(x=0, y=0, rs=0, cal=0):
    global mx, mn
    if cal == 0:
        rs += int(bd[x][y])
    elif cal == 1:
        rs -= int(bd[x][y])
    elif cal == 2:
        rs *= int(bd[x][y])
    if x == n-1 and y == n-1:
        mx = max(mx, rs)    
        mn = min(mn, rs)
        return
    for a,b in near:
        xi, yi = x+a, y+b
        if 0 <= xi < n and 0 <= yi < n:
            if bd[x][y].isdigit():
                go(xi,yi,rs,3)
            elif bd[x][y] == '+':
                go(xi,yi,rs,0)
            elif bd[x][y] == '-':
                go(xi,yi,rs,1)
            elif bd[x][y] == '*':
                go(xi,yi,rs,2)


n = int(input())
bd = [list(input().split()) for i in range(n)]
mn = 999999999999999999999
mx = -999999999999999999999
go()
print(mx, mn)