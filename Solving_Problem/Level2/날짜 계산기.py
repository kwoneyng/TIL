for i in range(int(input())):
    M_D = {}
    for j in (1, 3, 5, 7, 8, 10, 12):  # 얘네들은 31일까지 있는 애들입니다.
        M_D[j] = 31
    for j in (4, 6, 9, 11):  # 얘네들은 30일까지 있는 애들입니다.
        M_D[j] = 30
    M_D[2] = 28  # 2월은 28일까지
    mon, day, n_mon, n_day = list(map(int, input().split()))  # 변수를 받아와서 저장해줬습니다.
    d_day = 0
    for j in range(mon, n_mon):  # 계산과정입니다.
        d_day += M_D[j]
    d_day += n_day - day + 1
    print(f'#{i+1} {d_day}')  # 놀랍게도 얼마전에 배운 datetime으로 아무것도 안하고 풀을수가 있습니다.