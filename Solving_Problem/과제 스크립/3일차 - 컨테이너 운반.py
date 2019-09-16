for T in range(int(input())):
    n, m = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    flag = [0]*m
    rs = 0
    for t in range(m):
        for w in range(len(wi)):
            if ti[t] >= wi[w]:
                rs += wi[w]
                flag[t] = 1
                del wi[:w+1]
                break
        if flag[t] == 0:
            break
    print('#{}'.format(T+1), rs)