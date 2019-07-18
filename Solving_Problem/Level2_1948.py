for i in range(int(input())):
    M_D = {}
    for j in (1, 3, 5, 7, 8, 10, 12):
        M_D[j] = 31
    for j in (4, 6, 9, 11):
        M_D[j] = 30
    M_D[2] = 28
    mon, day, n_mon, n_day = list(map(int, input().split()))
    d_day = 0
    for j in range(mon, n_mon):
        d_day += M_D[j]
    d_day += n_day - day + 1
    print(f'#{i+1} {d_day}')