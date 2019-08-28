for T in range(int(input())):
    n = int(input())
    bd = []
    rs = 0
    for i in range(n):
        bd.append([int(i) for i in input()])
    stack = []
    vis = []
    near = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(n):
        vis.append([0 for i in range(n)])
    for x in range(n):
        for y in range(n):
            if bd[x][y] == 2:
                stack.append([x, y])
                break
    while stack:
        x, y = stack.pop()
        vis[x][y] = 1
        for a, b in near:
            if 0 <= x+a < n and 0 <= y+b < n:
                if vis[x+a][y+b] == 0:
                    if bd[x+a][y+b] == 0:
                        stack.append([x+a, y+b])
                    elif bd[x+a][y+b] == 3:
                        rs = 1
                        break
    print('#{} '.format(T+1),end='')
    print(rs)    

