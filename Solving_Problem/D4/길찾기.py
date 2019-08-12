import time

def fnr(ls, end=0):
    # time.sleep(0.1)
    if end == 99:
        return 1
    #보니까 0으로 시작하는게 1개가 아님
    for i in range(1, len(ls)):
        if ls[0][1] == ls[i][0]:
            if fnr(ls[i:], ls[i][1]) == 1:
                return 1
    return 0

for T in range(10):
    S, N = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    Bl = []
    for i in range(0,len(ls),2):
        su = []
        for j in range(2):
            su.append(ls[i+j])
        Bl.append(su)
    Bl = sorted(Bl,key = lambda x:x[0])
    cnt = 0
    start = []
    for j in Bl:
        if 0 in j:
            start.append(j)
            cnt += 1
    del Bl[:cnt]
    rs = []
    for k in start:
        sl = [k] + Bl
        rs.append(fnr(sl))
    if 1 in rs:
        rs = 1
    else :
        rs = 0
    print(f'#{T+1} ',end='')
    print(rs)
