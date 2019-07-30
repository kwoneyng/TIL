import time

for T in range(int(input())):
    print('-------------')
    P, Pa, Pb = list(map(int, input().split()))
    l = 1
    r = P
    m = 0
    n = 0
    for i in range(1, P):
        time.sleep(0.5)
        ca = int((l+r)/2)
        print(ca)
        if ca == Pa :
            n= i
            break
        else :
            l = ca
    for j in range(1, P):
        cb = int((l+r)/2)
        if cb == Pb :
            m = j
            break
        else :
            r = cb
    if n == 0 :
        n = P
    if m == 0 :
        m = P

    if n < m :
        print('A')
    elif n > m :
        print('B')
    else :
        print('0')
    print(n, m)

