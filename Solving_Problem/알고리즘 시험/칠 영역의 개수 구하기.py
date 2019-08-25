for T in range(int(input())):
    n, k = map(int, input().split())
    bd = []
    rs = 0
    for i in range(n+1):
        bd.append([0 for i in range(n+1)])
    for i in range(k):
        x_1, y_1, x_2, y_2 = map(int, input().split())
        for a in range(x_1, x_2+1):
            for b in range(y_1, y_2+1):
                bd[a][b] = 1
    for i in bd:
        rs += i.count(1)
    print('#{} '.format(T+1),end='')
    print(rs)