import sys
sys.setrecursionlimit(10000) 

def oxi(start_x=0, start_y=0):
    vis[start_x][start_y] = 1
    if bd[start_x][start_y] == 1:
        if [start_x, start_y] not in distroy:
            distroy.append([start_x, start_y])
        return 0
    for a, b in near:
        if 0 <= start_x+a < x and 0 <= start_y+b < y:
            if vis[start_x+a][start_y+b] == 0:
                oxi(start_x+a, start_y+b)


def reset():
    for row in range(x):
        for col in range(y):
            vis[row][col] = 0


def melt():
    for x, y in distroy:
        bd[x][y] = 0


def check_zero(ls):
    rs = 0
    for i in ls:
        rs += sum(i)
    if rs == 0:
        return True
    else:
        return False


x, y = map(int, input().split())
bd = []
distroy = []
near = [[-1,0], [0, 1], [1, 0], [0,-1]]
for row in range(x) :
    bd.append(list(map(int, input().split())))
vis = []
for row in range(x+1):
    vis.append([0 for i in range(y+1)])
cnt = 0
while True:
    cnt += 1
    # print(bd)
    oxi()
    reset()
    # print(distroy)
    melt()
    if check_zero(bd):
        break
    else :
        distroy = []
    
print(cnt)
print(len(distroy))