for tc in range(int(input())):
    N, M = map(int, input().split())

    board = [[0]*N for n in range(N)]

    for m in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1

    cnt = 0    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))
