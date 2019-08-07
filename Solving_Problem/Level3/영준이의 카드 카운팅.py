for T in range(int(input())):
    pro = input()
    get = []
    g_set = set()
    for i in range(len(pro)//3):
        get.append(pro[i*3:i*3+3])
    g_set.update(get)
    S, D, H, C = (13,13,13,13)
    print('#{} '.format(T+1), end='')
    if len(g_set) == len(get):
        for i in get:
            if i[0] == 'S':
                S -= 1
            elif i[0] == 'D':
                D -= 1
            elif i[0] == 'H':
                H -= 1
            else:
                C -= 1
        print(S, D, H, C)
    else : 
        print('ERROR')