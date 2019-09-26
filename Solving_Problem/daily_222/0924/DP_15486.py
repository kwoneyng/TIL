def pick(start):
    global n, mx
    for i in range(1,n+2):
        if DP[i] < DP[i-1]:
            DP[i] = DP[i-1]
        if i > n:
            break
        day, pay = ls[i]
        pay_day = i+day
        total_pay = DP[i]+pay
        if pay_day <= n+1:
            if DP[pay_day] < total_pay:
                DP[pay_day] = total_pay



n = int(input())
ls = [0]+[list(map(int,input().split())) for i in range(n)]
DP = [0]*(n+2)
pick(1)
print(DP[-1])
