def island(x, y):
    stack.append((x, y))
    while len(stack) > 0:
        ix, iy = stack.pop()
        board[ix][iy] = '0'
        if 1 <= ix < N-1 and 1 <= iy < N-1:
            for i in range(ix-1, ix+2):
                for j in range(iy-1, iy+2):
                    if board[i][j] != '0':
                        stack.append((i, j))
        elif 1 <= iy < N-1 and ix == 0:
            for i in range(ix, ix+2):
                for j in range(iy-1, iy+2):
                    if board[i][j] != '0':
                        stack.append((i, j))
        elif 1 <= ix < N-1 and iy == 0:
            for i in range(ix-1, ix+2):
                for j in range(iy, iy+2):
                    if board[i][j] != '0':
                        stack.append((i, j))
        elif 1 <= iy < N-1 and ix == N-1:
            for i in range(ix-1, ix+1):
                for j in range(iy-1, iy+2):
                    if board[i][j] != '0':
                        stack.append((i, j))
        elif 1 <= ix < N-1 and iy == N-1:
            for i in range(ix-1, ix+2):
                for j in range(iy-1, iy+1):
                    if board[i][j] != '0':
                        stack.append((i, j))


for tc in range(int(input())):
    N = int(input())
    board = [input().split() for n in range(N)]

    stack = []

    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != '0':
                cnt += 1
                island(i, j)
    print('#{} {}'.format(tc+1, cnt))