for T in range(int(input())):
    n, e = map(int, input().split())
    e_ls = []
    fw = [[] for i in range(n+1)]
   
    for i in range(e):
        e_ls.append(list(map(int, input().split())))
    s, g = map(int, input().split())

    for i in e_ls:
        fw[i[0]] += [i[1]]
        fw[i[1]] += [i[0]]
    q = [[0,s]]
    vis = [0 for i in range(n+1)]
    vis[s] = 1
    is_fin = False
    while q :
        dept, point = q.pop(0)
        for i in fw[point]:
            if i == g:
                print('#{}'.format(T+1), dept+1)
                is_fin = True
                break
            if vis[i] == 0:
                q.append([dept+1, i])
                vis[i] = 1
        if is_fin :
            break
    if is_fin != 1 :
        print('#{}'.format(T+1), 0)

