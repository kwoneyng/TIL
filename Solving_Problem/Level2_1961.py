for i in range(int(input())):
    N = int(input())
    XY = []
    for j in range(N):
        XY.append(list(map(int, input().split())))
    print(f'#{i+1}', end = '')
    for j in range(N):
        print('')
        for k in range(N):
            print(XY[N-k-1][j], end = '')
        print(' ',end = '')
        for k in range(N):
            print(XY[N-j-1][N-k-1], end = '')
        print(' ',end = '')
        for k in range(N):
            print(XY[k][N-j-1], end = '')
    print('')
