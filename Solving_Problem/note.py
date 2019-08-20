for T in range(1):
    v, e = list(map(int, input().split()))
    ls_e = []
    N = list(map(int, input().split()))
    al = set(N)
    while len(N) > 0 :
        su = []
        for i in range(2):
            su.append(N.pop(0))
        ls_e.append(su)
    print(f'ls_e={ls_e}')  # 순서쌍
