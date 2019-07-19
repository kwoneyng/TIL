for i in range(int(input())):
    N = int(input())
    s = []
    o = 0
    print(f'#{i+1}')
    for j in range(N):
        x = []
        for k in range(N):
            x.append(0)
        s.append(x)
    a = list(range(1, N*N+1))
    c = N
    p = 0
    while(c>0):
        if o == 0 :
            for k in range(c):
                s[p][k+p] = a[0]
                a.pop(0)
            c -= 1
            o = 1
        elif o == 1 :
            for k in range(c):
                s[k+p+1][N-1-p] = a[0]
                a.pop(0)
            o = 2
        elif o == 2 :
            for k in range(c):
                s[N-1-p][N-2-k-p] = a[0]
                a.pop(0)
            c -= 1
            o = 3
        elif o == 3 :
            for k in range(c):
                s[N-2-p-k][p] = a[0]
                a.pop(0)
            p += 1
            o = 0
    for x in range(N) :
        for y in range(N):
            print(s[x][y], end=' ')
        print('')
