for T in range(10):
    n, st = map(int, input().split())
    e = list(map(int, input().split()))
    e_set = []
    queue = []
    dept = 0
    dept_set = [[] for i in range(101)]
    for i in range(0,len(e), 2):
        su = []
        for j in range(2):
            su.append(e[i+j])
        e_set.append(su)
    ls = [[] for i in range(n+1)]
    vis = [0 for i in range(n+1)]
    for i in e_set:
        ls[i[0]].append(i[1])
    queue.append([dept, st])
    vis[st] = 1
    while queue:
        chk = queue.pop(0)
        dept_set[chk[0]].append(chk[1])
        ls_chk = list(ls[chk[1]])
        for i in ls_chk:
            if vis[i] == 0:
                queue.append([chk[0]+1, i])
                vis[i] = 1
    print('#{}'.format(T+1), max(dept_set[chk[0]]))
