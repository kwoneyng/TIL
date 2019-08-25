def sum_edge(ii, jj, k):
    ssum = 0
    for i in range(ii, ii+k):
        ssum += board[i][jj] + board[i][jj+k-1]
    for j in range(jj+1, jj+k-1):
        ssum += board[ii][j] + board[ii+k-1][j]
    return ssum


for tc in range(int(input())):
    N, M, K = map(int, input().split())

    board = [list(map(int, input().split())) for n in range(N)]
    sum_list = []

    for i in range(N-K+1):
        for j in range(M-K+1):
            sum_list.append(sum_edge(i, j, K))

    result = max(sum_list)
    print('#{} {}'.format(tc+1, result))
