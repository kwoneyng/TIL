for q in range(10):
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
    res = ' '.join(ls[0 : 10])
    print(f'#{q+1} {res}')
