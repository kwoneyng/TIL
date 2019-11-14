def solve(rs, cnt=1):
    global mx, mn
    if cnt == n:
        mn = min(mn, rs)
        mx = max(mx, rs)
        return
    for i in range(4):
        if i == 0:
            if c[i] > 0:
                c[i] -= 1
                solve(rs+su[cnt],cnt+1)
                c[i] += 1
        elif i == 1:
            if c[i] > 0:
                c[i] -= 1
                solve(rs-su[cnt],cnt+1)
                c[i] += 1
        elif i == 2:
            if c[i] > 0:
                c[i] -= 1
                solve(rs*su[cnt],cnt+1)
                c[i] += 1
        elif i == 3:
            if c[i] > 0:
                c[i] -= 1
                solve(int(rs/su[cnt]),cnt+1)
                c[i] += 1


for t in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    mn = 999999999999999999999999999
    mx = -9999999999999999999999999999
    su = list(map(int,input().split()))
    solve(su[0])
    print(f'#{t+1}', end=' ')
    print(mx-mn)