import time

for T in range(int(input())):
    P, Pa, Pb = list(map(int, input().split()))
    l_a, r_a, l_b, r_b  = (1, P, 1, P)
    cnt_a, cnt_b = (0, 0)
    rs = ''
    for i in range(P):
        cnt_a += 1
        c_a = int((l_a+r_a)/2)
        if c_a == Pa :
            break
        elif c_a < Pa :
            l_a = c_a
        else :
            r_a = c_a
    for j in range(P):
        cnt_b += 1
        c_b = int((l_b+r_b)/2)
        if c_b == Pb :
            break
        elif c_b < Pb :
            l_b = c_b
        else :
            r_b = c_b

    if cnt_a > cnt_b :
        rs = 'B'
    elif cnt_a < cnt_b:
        rs = 'A'
    else :
        rs = '0'
    print('#{0} {1}'.format(T+1, rs))


