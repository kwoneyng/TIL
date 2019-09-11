def nqueen(ls, n):
    global cnt
    if len(ls) == n:
        cnt += 1
        return 0
    s = [i for i in range(n)]
    for i in range(len(ls)):
        if ls[i] in s:
            s.remove(ls[i])
        check = len(ls) - i
        if ls[i] + check in s:
            s.remove(ls[i]+check)
        if ls[i] - check in s:
            s.remove(ls[i]-check)
    if s:
        for i in s:
            ls.append(i)
            nqueen(ls, n)
            ls.pop()
for T in range(int(input())):
    n = int(input())
    cnt = 0
    nqueen([], n)
    print('#{} {}'.format(T+1, cnt))