def fill_in(x=1):
    global cnt
    nxls = nxt_ls[x]
    if nxls:
        fill_in(nxls[0])
        tree[x] = cnt
        cnt += 1
        if len(nxls) > 1:
            fill_in(nxls[1])
    else:
        tree[x] = cnt
        cnt += 1



for t in range(int(input())):
    n = int(input())
    tree = [0]*(n+1)
    nxt_ls = [[] for i in range(n+1)]
    cnt = 1
    j = 1
    for i in range(2,n+1):
        nxt_ls[j].append(i)
        if len(nxt_ls[j]) == 2:
            j += 1
    fill_in()
    print('#{}'.format(t+1),tree[1],tree[n//2])
    