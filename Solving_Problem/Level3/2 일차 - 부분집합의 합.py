ls = [i for i in range(1,13)]

for T in range(int(input())):
    n, k = list(map(int, input().split()))
    su_set = []
    rs_set = []
    cnt = 0
    for i in range(1<<len(ls)):
        su = []
        for j in range(len(ls)):
            if i & (1<<j):
                su += [ls[j]]
        su_set.append(su)
    # print(su_set)
    for l in su_set:
        if len(l) == n :
            rs_set.append(l)
    # print(rs_set)
    for g in rs_set:
        if sum(g) == k:
            cnt += 1
    print(f'#{T+1} {cnt}')
    