def make(n, ls=[], op=0, flr=0):
    global mn
    if len(ls) == n:
        if mn > op:
            mn = op
            rs.append(op)
        return 1
    for i in range(n):
        if i not in ls :
            ls.append(i)
            op += bd[flr][i]
            if op > mn :
                ls.pop()
                op -= bd[flr][i]
                continue
            else :
                make(n, ls, op, flr+1)
            ls.pop()
            op -= bd[flr][i]
        

for T in range(int(input())):
    n = int(input())
    bd = []
    rs= []
    mn = 10000000
    for i in range(n):
        bd.append(list(map(int, input().split())))
    make(n)
    print('#{} '.format(T+1),end='')
    print(mn)
    print(rs)
