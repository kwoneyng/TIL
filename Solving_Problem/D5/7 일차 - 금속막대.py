for T in range(int(input())):
    N = int(input())
    ls = list(map(int, input().split()))
    var = []
    for i in range(N):
        var.append((ls.pop(0), ls.pop(0)))
    start = []
    start += [var.pop()]
    while len(var) > 0 :
        for i in var:
            if i[0] == start[-1][1]:
                start.append(i)
                var.remove(i)
                break
            elif i[1] == start[0][0]:
                start.insert(0,i)
                var.remove(i)
                break
    print(f'#{T+1} ',end='')
    for s in start:
        print(s[0], s[1], end=' ')
    print('')
        