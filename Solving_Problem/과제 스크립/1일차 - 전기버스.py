for T in range(int(input())):
    K, N, M = map(int, input().split())
    M_s = list(map(int, input().split()))
    M_s.append(N)
    stop = 0
    K_re = K
    cnt = 0
    for i in range(N):
        print('K = {}'.format(K))
        if stop < len(M_s):
            if i == M_s[stop]:
                stop += 1
                if K < M_s[stop]-i:
                    print('-------------')
                    print(i)
                    cnt += 1
                    K = K_re-1
                else :
                    K -= 1    
            else :
                K -= 1
            if K < 0 :
                cnt = 0
                break
        else :
            K -= 1
    print('#{0} {1}'.format(T+1, cnt))
