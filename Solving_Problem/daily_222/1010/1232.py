for t in range(2):
    n = int(input())
    nxt_ls = [[] for i in range(n+1)]
    tree = ['']*(n+1)
    for i in range(1,n+1):
        data = list(input().split())
        nxt_ls[i].extend(data[2:])
        if data[1].isdecimal():
            tree[i] = int(data[1])
        else:
            tree[i] = data[1]
    print(tree)