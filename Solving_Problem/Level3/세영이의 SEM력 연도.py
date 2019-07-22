for T in range(int(input())):
    S, E, M = list(map(int, input().split()))
    S_c, E_c, M_c = (0, 0, 0)
    y_c = 0
    print(f'#{T+1} ', end='')
    for i in range(365*24*29 + 1):
        if S_c == 366:
            S_c = 1
        if E_c == 25:
            E_c = 1
        if M_c == 30:
            M_c = 1
        if S_c == S  and E == E_c and M == M_c :
            print(y_c)
            break
        y_c += 1
        S_c += 1
        E_c += 1
        M_c += 1
        