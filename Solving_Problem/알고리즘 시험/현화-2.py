T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    board = []
    for _ in range(N):
        board += [list(map(int, input().split()))]
    res = []
    for i in range(len(board)-K+1):
        for j in range(len(board)-K+1):
            s = []
            for k in range(K):
                s.append(board[i][j+k])
            for k in range(1, K):
                s.append(board[i+k][j+K-1])
                s.append(board[i+k][j])
                s.append(board[i+K-1][j+k])
            s.pop()
            res.append(sum(s))

    print('#{} {}'.format(t+1, max(res)))
