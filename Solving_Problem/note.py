for T in range(1):
    v, e = map(int, input().split())
    st = list(map(int, input().split()))
    tar = []
    while len(st) > 0: 
        su = []
        for i in range(2):
            su.append(st.pop(0))
        tar.append(su)
    visit = ['X']+[0] * (len(tar))
    nt_ls = [[] for i in range(len(tar)+1)]
    stack = []
    for i in tar:
        nt_ls[i[0]] += [i[1]]
        visit[i[1]] += 1
    print(nt_ls, visit)
    while True:
        for i in range(len(visit)):
            if visit[i] == 0:
                visit[i] = 'X'
                stack.extend(nt_ls[i])
    print(visit)