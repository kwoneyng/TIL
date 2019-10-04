for t in range(int(input())):
    ls = list(map(int, input().split()))
    uls = []
    for i in range(10):
        if ls[i] == 1:
            uls.append(i)
    x = input()
    rs = []
    q = [[x,0]]

    while q:
        chk, cnt = q.pop(0)
        flag = 0
        for i in chk:
            if not ls[int(i)]:
                flag = 1
                break
        if flag == 0:
            cnt += len(chk)
            rs.append(cnt)
        else:
            for i in range(len(uls)):
                if uls[i] > 1:
                    for j in range(1,len(chk)):
                        pi = ['1']*j
                        pi = int(''.join(pi))
                        if int(chk) % uls[i]*pi == 0:
                            su = str(int(chk) // (uls[i]*pi)) 
                            q.append([su, cnt+j+1])


    print('#{}'.format(t+1),end=' ')
    if rs:
        print(min(rs)+1)
    else:
        print(-1)