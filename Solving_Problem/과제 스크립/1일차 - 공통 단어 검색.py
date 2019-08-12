for T in range(int(input())):
    n, m = list(map(int, input().split()))
    n_ls=[]
    m_ls=[]
    for i in range(n):
        n_ls.append(input())
    for j in range(m):
        m_ls.append(input())
    dp = [0]*len(n_ls)
    cnt = 0
    for k in n_ls:
        for p in m_ls:
            if k == p:
                dp[cnt] += 1
        cnt += 1
    rs = 0
    for last in dp:
        if last > 0 :
            rs += 1
    print(f'#{T+1} ',end='')
    print(rs)
