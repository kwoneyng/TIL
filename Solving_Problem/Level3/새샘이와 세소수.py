for T in range(int(input())):
    n = int(input())
    board = [False, False, True]+[True] * n
    sosu = []
    for i in range(1, len(board)):
        if board[i] == True:
            for l in range(2*i, len(board), i):
                board[l] = False
            sosu.append(i)
    cnt = 0
    for x in sosu:
        for y in sosu[sosu.index(x):]:
            for z in sosu[sosu.index(y):]:
                if x + y + z == n:
                    cnt += 1
    print('#{}'.format(T+1), end=' ')
    print(cnt)

    