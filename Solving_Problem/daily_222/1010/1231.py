def prt_wd(x=1):
    global rs
    nxls = nxt_ls[x]
    if nxls:
        prt_wd(nxls[0])
        rs += tree[x]
        if len(nxls) > 1:
            prt_wd(nxls[1])
    else:
        rs += tree[x]


for t in range(10):
    n = int(input())
    nxt_ls = [[] for i in range(n+1)]
    tree = ['' for i in range(n+1)]
    rs = ''
    for i in range(n):
        data = list(input().split())
        tree[int(data[0])] = data[1]
        if len(data) > 2:
            nxt_ls[int(data[0])].extend(map(int,data[2:]))
    prt_wd()
    print('#{}'.format(t+1),rs)

