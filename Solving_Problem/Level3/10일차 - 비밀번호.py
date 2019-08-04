for T in range(10):
    N, su = list(map(str, input().split()))
    ls = [str(i)*2 for i in range(10)]
    cnt = 0
    for j in range(int(N)):
        for k in ls:
            cnt += 1
            if k in su:
                su = su.replace(k,'')
                cnt = 0
                break
        if cnt > 9 :
            break
    print('#{0} {1}'.format(T+1, su))