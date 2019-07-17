for i in range(int(input())):
    N = int(input())
    snail = []
    order = 0
    print(f'#{i+1}')
    for j in range(N):
        x = []
        for k in range(N):
            x.append(0)
        snail.append(x)
    a = list(range(1, N*N+1))
    count = N
    padding = 0
    while(count>0):
        if order == 0 :
            for k in range(count):
                snail[padding][k+padding] = a[0]
                a.pop(0)
            count -= 1
            order = 1
        elif order == 1 :
            for k in range(count):
                snail[k+padding+1][N-1-padding] = a[0]
                a.pop(0)
            order = 2
        elif order == 2 :
            for k in range(count):
                snail[N-1-padding][N-2-k-padding] = a[0]
                a.pop(0)
            count -= 1
            order = 3
        elif order == 3 :
            for k in range(count):
                snail[N-2-padding-k][padding] = a[0]
                a.pop(0)
            padding += 1
            order = 0
    for x in range(N) :
        for y in range(N):
            print(snail[x][y], end=' ')
        print('')

