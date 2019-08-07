def result(*ls):
    mn = ls[0]
    mx = 0
    for i in ls:
        if i > mx :
            mx = i
        elif i < mn :
            mn = i
    return mx - mn

for T in range(int(input())):
    t_no = int(input())
    ls = list(map(int, input().split()))
    rs = result(*ls)
    print('#{0} {1}'.format(T+1, rs))

