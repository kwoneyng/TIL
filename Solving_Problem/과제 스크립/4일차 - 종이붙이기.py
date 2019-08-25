def my_fib(n):
    f = [0, 1]
    if n >= 2:
        su = 0
        for i in range(2, n+1):
            if i % 2 == 1:
                f.append(sum(f)+1)
            else :
                f.append(sum(f)+2)
    return f[n]


for T in range(int(input())):
    N = int(input())
    print(f'#{T+1} ',end='')
    print(my_fib(N//10))
    