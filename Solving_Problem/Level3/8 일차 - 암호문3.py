for q in range(2):
    t_no = int(input())
    ls = []
    ls = input().split()
    c_no = int(input())
    c_ls = input().split()
    for i in range(c_no):
        wh = c_ls.pop(0)
        if wh == 'I':
            idx = int(c_ls.pop(0))
            n = int(c_ls.pop(0))
            for i in range(n):
                a = c_ls.pop(0)
                ls.insert(idx+i, a)
        if wh == 'D':
            idx = int(c_ls.pop(0))
            dn = int(c_ls.pop(0))
            del ls[idx:idx+dn]
        if wh == 'A':
            n = int(c_ls.pop(0))
            for k in range(n):
                ls.append(c_ls.pop(0))
    res = ' '.join(ls[0 : 10])
    print(f'#{q+1} {res}')
