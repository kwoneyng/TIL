for T in range(int(input())):
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    a_ls = [a]
    b_ls = [b]
    for i in range(len(a)):
        if a[i] == 0:
            a_ls.append(a[:i]+[1]+a[i+1:])
        elif a[i] == 1:
            a_ls.append(a[:i]+[0]+a[i+1:])
    for i in range(len(b)):
        if b[i] == 0:
            b_ls.append(b[:i]+[1]+b[i+1:])
            b_ls.append(b[:i]+[2]+b[i+1:])
        elif b[i] == 1:
            b_ls.append(b[:i]+[0]+b[i+1:])
            b_ls.append(b[:i]+[2]+b[i+1:])
        elif b[i] == 2:
            b_ls.append(b[:i]+[0]+b[i+1:])
            b_ls.append(b[:i]+[1]+b[i+1:])
    for i in range(len(a_ls)-1,-1,-1):
        if a_ls[i][0] == 0:
            a_ls.pop(i)
    for i in range(len(b_ls)-1,-1,-1):
        if b_ls[i][0] == 0:
            b_ls.pop(i)

    for i in range(len(a_ls)):
        a_ls[i] = sum([a_ls[i][j]*(2**(len(a_ls[i])-j-1)) for j in range(len(a_ls[i]))])

    for i in range(len(b_ls)):
        b_ls[i] = sum([b_ls[i][j]*(3**(len(b_ls[i])-j-1)) for j in range(len(b_ls[i]))])

    for i in a_ls:
        for j in b_ls:
            if i == j:
                print('#{}'.format(T+1), i)