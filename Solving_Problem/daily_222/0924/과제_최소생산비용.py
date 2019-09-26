def mk_set(ls=[],rs=0,flr=0):
    global mn
    if len(ls) == n:
        if rs < mn:
            mn = rs
            return 0
    for i in range(n):
        if i not in ls:
            if rs+bd[flr][i] < mn:
                mk_set(ls+[i],rs+bd[flr][i],flr+1)

for t in range(int(input())):
    n = int(input())
    bd = [list(map(int,input().split())) for i in range(n)]
    mn = 10000000000
    mk_set()
    print('#{}'.format(t+1),mn)