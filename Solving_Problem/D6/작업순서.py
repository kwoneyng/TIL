for T in range(10):
    v, e = map(int, input().split())
    st = list(map(int, input().split()))
    tar = []
    while len(st) > 0: 
        su = []
        for i in range(2):
            su.append(st.pop(0))
        tar.append(su)
    visit = ['X']+[0] * (v)
    nt_ls = [[] for i in range(v+1)]
    stack = []
    for i in tar:
        nt_ls[i[0]] += [i[1]]
        visit[i[1]] += 1
    rs = ''
    for i in range(v):
        if visit[i] == 0:
            visit[i] = 'X'
            stack.extend(nt_ls[i])
            rs += str(i) + ' '
    while stack :
        chk = stack.pop()
        if type(visit[chk]) == int:
            visit[chk] -= 1
            if visit[chk] == 0:
                visit[chk] = 'X'
                stack.extend(nt_ls[chk])
                rs += str(chk) + ' '
    print(f'#{T+1} ',end='')        
    print(rs)