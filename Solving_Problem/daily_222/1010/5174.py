def cnt_nd(x):
    global cnt
    cnt += 1
    for i in nxt_ls[x]:
        cnt_nd(i)


for t in range(int(input())):
    e, n = map(int,input().split())
    data = list(map(int,input().split()))
    nxt_ls = [[] for i in range(e+2)]
    cnt = 0
    for i in range(e):
        nxt_ls[data[i*2]].append(data[i*2+1])
    cnt_nd(n)
    print('#{}'.format(t+1), cnt)