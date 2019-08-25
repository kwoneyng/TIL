def bfs(y, x):
    global board
    global N

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    board[y][x] = -1
    queue = [x, y]
    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        for idx in range(8):
            xi = x + dx[idx]
            yi = y + dy[idx]
            if 0 <= xi < N and 0 <= yi < N and board[yi][xi] >= 1:
                board[yi][xi] = -1
                queue.append(xi)
                queue.append(yi)
    return 1

for case in range(1, int(input()) + 1):
    N = int(input())
    board = []
    cnt = 0
    for i in range(N):
        board.append(list(map(int, input().split())))

    for j in range(N):
        for i in range(N):
            if board[j][i] >= 1:
                cnt += bfs(j, i) 

    print(f'#{case} {cnt}')
