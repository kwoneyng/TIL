def f_mx(ls):
    mx = ls[0]
    for i in ls:
        if i > mx:
            mx = i
    return mx

def f_mn(ls):
    mn = ls[0]
    for i in ls:
        if i < mn:
            mn = i
    return mn

def f_idx(ls, x):
    can = 0
    for i in range(len(ls)):
        if ls[i] == x:
            return i


for T in range(10):
    N = int(input())
    a = list(map(int, input().split()))
    for p in range(N):
        a[f_idx(a, f_mx(a))] -= 1
        a[f_idx(a, f_mn(a))] += 1
    print('#{} '.format(T+1), end='')
    print(a[f_idx(a,f_mx(a))]-a[f_idx(a,f_mn(a))])
    