n = int(input())
bd = [list(map(int,input().split())) for i in range(n)]
can = [[1]*n for i in range(n)]

rs = 0

for k in range(n):
    for x in range(n):
        for y in range(n):
            if x != k and y != k and x != y:
                if bd[x][y] == bd[x][k] + bd[k][y]:
                    can[x][y] = 0
                elif bd[x][y] > bd[x][k] + bd[k][y]:
                    rs = -1
        else:
            continue
        break
    else:
        continue
    break
# for i in can:
#     print(i)

if rs == 0:
    for x in range(n):
        for y in range(x,n):
            if can[x][y] == 1:
                rs += bd[x][y]
    print(rs)
else:
    print(rs)