for T in range(int(input())):
    a = int(input())
    xy = []
    p = []
    e = []
    rs = 0
    for i in range(a):
        ay, ax, ap, ae = list(map(int, input().split()))
        xy.append([ax*2, ay*2])
        p.append(ap)
        e.append(ae)
    
    while xy:
        que = []
        flag = 0
        dist = []
        for i in range(len(xy)-1,-1,-1):
            if p[i] == 0:
                xy[i][0] += 1

            elif p[i] == 1:
                xy[i][0] -= 1

            elif p[i] == 2:
                xy[i][1] -= 1

            elif p[i] == 3:
                xy[i][1] += 1
                    
            if -2001 < xy[i][0] < 2001 and -2001 < xy[i][1] < 2001:
                if xy[i] in que :
                    flag =1
                    if xy[i] not in dist:
                        dist.append(xy[i])
                else:
                    que.append(xy[i])
            else :
                xy.pop(i)
                e.pop(i)
                p.pop(i)

        if flag == 1:
            for i in dist:
                for j in range(len(xy)-1,-1,-1):
                    if xy[j] == i:
                        xy.pop(j)
                        p.pop(j)
                        rs += e.pop(j)
    print('#{}'.format(T+1), rs)