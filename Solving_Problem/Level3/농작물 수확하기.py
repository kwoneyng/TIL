for T in range(int(input())):
    n = int(input())
    bd = []
    for row in range(n):
        bd.append([int(i) for i in input()])
    mid = n//2
    rs = 0
    for i in range(mid):
        rs += sum(bd[i][mid-i:mid+i+1])
    j = 0
    for i in range(mid,n):
        rs += sum(bd[i][j:n-j])
        j += 1
    print('#{}'.format(T+1), rs)