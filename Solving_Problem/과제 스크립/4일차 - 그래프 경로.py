for T in range(int(input())):
    v, e = list(map(int, input().split()))
    ls_e = []
    for i in range(e):
        ls_e.append(list(map(int, input().split())))
    ls_e = sorted(ls_e,key=lambda x:x[0])
    s, g = list(map(int, input().split()))
    visit = [0]*(len(ls_e)+1)
    nt_ls = [[] for i in range(v+1)]
    stack = []
    print(visit)
    for i in ls_e:
        nt_ls[i[0]] += [i[1]]
    print(nt_ls)
    stack.append(s)
    rs = 0
    while stack :
        chk = stack.pop()
        stack.extend(nt_ls[chk])
        if g in stack:
            rs = 1
            break
    print(f'#{T+1} ',end='')
    print(rs)