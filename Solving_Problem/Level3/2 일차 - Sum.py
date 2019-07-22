for T in range(10):
    t_no = int(input())
    bd = []
    sum_set = []
    for i in range(100):
        bd.append(list(map(int, input().split())))
    for i in bd :
        sum_set.append(sum(i))
    bd_ro = list(map(list, zip(*bd)))
    for j in bd_ro :
        sum_set.append(sum(j))
    su, su_ro = (0, 0)
    for k in range(100):
        su += bd[k][k]
        su_ro += bd_ro[k][k]
    sum_set.append(su)
    sum_set.append(su_ro)
    print(f'#{T+1} {max(sum_set)}')


