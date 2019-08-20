for T in range(10):
    t_no, e = list(map(int, input().split()))
    ls_e = []
    s = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        su = []
        su.append(s[i])
        su.append(s[i+1])
        ls_e.append(su)
    vis = [0]*100
    nt_ls = [[] for i in range(100)]
    for i in ls_e:
        nt_ls[i[0]] += [i[1]]
    stack = [0]
    rs = 0
    while stack:
        chk = stack.pop()
        if vis[chk] == 0:
            vis[chk] += 1
            stack.extend(nt_ls[chk])
            if 99 in stack:
                rs = 1
                break
    print(f'#{T+1} ',end='')
    print(rs)