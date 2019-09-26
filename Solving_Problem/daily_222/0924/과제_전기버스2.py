for t in range(int(input())):
    data = list(map(int,input().split()))
    end = data.pop(0)-1
    k = data[0]
    stack = [[0,k,0]]
    mn = 100000
    while stack:
        dist, k, cnt = stack.pop()
        if cnt >= mn :
            continue
        elif dist == end:
            mn = cnt
            continue
        elif dist > 0:
            if k >= 0:
                stack.append([dist+1,-1+data[dist],cnt+1])
        if k-1 >= 0:
            stack.append([dist+1,k-1,cnt])
            
    print('#{}'.format(t+1),mn)

