for T in range(int(input())):
    n = int(input())
    bd = []
    for i in range(n):
        bd.append([int(i) for i in input()])
    for x in range(n):
        for y in range(n):
            if bd[x][y] == 2:
                start = [x, y]
    queue = [[0, start]]
    near = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    print('#{} '.format(T+1),end='')
    while queue :
        rs = 0
        a = queue.pop(0)
        st_x, st_y = a[1]
        dst = a[0]
        for x, y in near:
            if 0 <= st_x+x < n and 0 <= st_y+y < n:
                if bd[st_x+x][st_y+y] == 0:
                    bd[st_x+x][st_y+y] = 1
                    queue.append([dst+1, [st_x+x, st_y+y]])
                elif bd[st_x+x][st_y+y] == 3:
                    rs = dst
                    break
        if rs > 0 :
            break
    print(rs)

    

