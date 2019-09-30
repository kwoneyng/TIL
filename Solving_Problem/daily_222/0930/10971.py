def go(i,start,vis,rs=0):
    global mn
    if rs > mn:
        return
    elif len(vis) == n:
        if bd[start][i] == 0:
            return
        elif rs + bd[start][i] < mn:
            mn = rs+bd[start][i]
            return 
    for j in range(n):
        if j not in vis:
            if bd[start][j] != 0:
                go(i,j,vis+[j],rs+bd[start][j])


n = int(input())
bd = [list(map(int, input().split())) for i in range(n)]
mn = 99999999999999999999999999999999999999
for i in range(n):
    go(i,i,[i])
print(mn)