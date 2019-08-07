def change(N, cnt=0):
    no = 0
    if dp[cnt] > int(''.join(N)):
        return True
    dp[cnt] = int(''.join(N))
    
    if cnt == C:
        return True

    for i in range(len(N)):
        for j in range(i+1,len(N)):
            no += 1
            sw = N[:]
            sw[i], sw[j] = sw[j], sw[i]
            change(sw, cnt+1)
for T in range(int(input())):
    a, b = list(map(str, input().split()))
    N = list(a)
    C = int(b)
    dp=[0]*(C+1)
    change(N)
    
    print(f'#{T+1} ',end='')
    print(dp[-1])
