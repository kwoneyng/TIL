for t in range(int(input())):
    n, b = map(int,input().split())
    mn = 100000
    nls=[i for i in list(map(int,input().split()))]
    stack = []
    for i in range(n):
        stack.append([i,nls[i]])
    while stack:
        i, rs = stack.pop()
        if rs >= b:
            if mn > rs:
                mn = rs
                continue
        for j in range(i+1,n):
            if rs+nls[j] < mn:
                stack.append([j,rs+nls[j]])

    print('#{}'.format(t+1),mn-b) 
