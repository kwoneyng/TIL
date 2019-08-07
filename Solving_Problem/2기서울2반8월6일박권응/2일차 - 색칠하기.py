for T in range(int(input())):
    K = int(input())
    bd = []
    for x in range(10):
        bd.append([0]*10)
    for i in range(K):
        cr = list(map(int, input().split()))
        for c_x in range(cr[0], cr[2]+1):
            for c_y in range(cr[1], cr[3]+1):
                if bd[c_x][c_y] == 0 :
                    bd[c_x][c_y] = cr[4]
                elif bd[c_x][c_y] == cr[4]:
                    continue
                else :
                    bd[c_x][c_y] += cr[4]
    cnt = 0
    for row in bd:
        for x in row:
            if x == 3:
                cnt += 1
    print('#{0} {1}'.format(T+1, cnt))
