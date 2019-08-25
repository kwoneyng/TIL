T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(101)] for __ in range(101)]
    boxes = []
    for _ in range(M):
        boxes += [list(map(int, input().split()))]
    
    for box in boxes:
        newlist = [1 for _ in range(box[1],box[3]+1)]
        for i in range(box[0],box[2]+1):
            board[i][box[1]:box[3]+1] = newlist

    s = 0
    for i in board:
        s += i.count(1)

    print('#{} {}'.format(t+1, s))
