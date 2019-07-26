def look(*bd):
    can = set()
    for b in bd:
        for t_no in range(1,30):
            for i in range(100-t_no+1):
                t_di = t_no // 2
                if b[i:i+t_di] == b[i+t_no-1:i+t_no-t_di-1:-1]:
                    can.update({t_no})
    return can
for T in range(10):
    N = int(input())
    bd =[]
    ro_bd = []
    for a in range(100):
        bd.append(input())
    ro_bd = list(map(list, zip(*bd)))
    X = look(*bd)
    Y = look(*ro_bd)
    print(f'#{T+1} {max(X|Y)}')