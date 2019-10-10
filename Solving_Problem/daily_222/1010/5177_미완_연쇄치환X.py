def search(x,rs=0):
    global rs_fin
    if x == 1:
        rs_fin = rs
        return
    else:
        nxt = rvs_nxt_ls[x][0]
        search(nxt,rs+tree[nxt])


for t in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    nxt_ls = [[] for i in range(n+1)]
    rvs_nxt_ls = [[] for i in range(n+1)]
    rs_fin = 0
    j = 1
    for i in range(2,n+1):
        nxt_ls[j].append(i)
        rvs_nxt_ls[i].append(j)
        if len(nxt_ls[j]) == 2:
            j += 1
    

    tree = [0]
    for i in range(len(data)):
        tree.append(data[i])
        if len(tree) > 2:
            pre_index = rvs_nxt_ls[len(tree)-1][0]
            if tree[-1] < tree[pre_index]:
                tree[-1],tree[pre_index] = tree[pre_index], tree[-1]
    search(n)
    print('#{}'.format(t+1), rs_fin)
