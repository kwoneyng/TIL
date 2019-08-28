def go(start_x=0, start_y=0):
    global cnt
    for i in range(n):
        for j in range(n):
            vis[i][j] = 1
            if bd[i][j] == 1:
                cnt += 1
                return grouping(i, j)

def grouping(start_x, start_y):
    bd[start_x][start_y] = cnt
    for x, y in near:
        if vis[start_x+x][start_y+y] == 0:
            if bd[start_x+x][start_y+y] ==1:
                if 0 <= start_x+x < n and 0 <= start_y+y < n:
                    grouping(start_x+x,start_y+y)


def alchk():
    rs = 0
    for i in bd:
        rs += bd.count(1)
    if rs == 0 :
        return False
    else :
        return True

                



n = int(input())
bd = []
for i in range(n):
    bd.append([int(i) for i in input()])
print(bd)
vis = []
for i in range(n):
    vis.append([0 for i in range(n)])
near = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 1
go()
print(bd)
print(cnt)