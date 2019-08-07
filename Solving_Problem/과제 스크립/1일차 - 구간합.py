for T in range(int(input())):
    N, M = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    sum_set = []
    for x in range(N-M+1):
        su = 0
        for i in range(x, M+x):
            su += ls[i]
        sum_set.append(su)
    mx = 0
    mn = sum_set[0]
    for q in sum_set:
        if q > mx:
            mx = q
    for p in sum_set:
        if p < mn:
            mn = p
    print('#{0} {1}'.format(T+1, mx-mn))
