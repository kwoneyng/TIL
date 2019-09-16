for t in range(int(input())):
    n = int(input())
    se = [list(map(int,input().split())) for i in range(n)]
    se.sort(key=lambda x:x[1])
    last = 0
    cnt = 0
    for i in range(n):
        if last <= se[i][0]:
            last = se[i][1]
            cnt += 1
    print('#{}'.format(t+1),cnt)