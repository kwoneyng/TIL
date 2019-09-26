def setting(ls=[],flr=0,rs=1):
    global mx
    if flr == n:
        if rs > mx:
            mx = rs
        return 0

    for i in range(n):
        if i not in ls:
            if rs*bd[flr][i] > mx:
                setting(ls+[i],flr+1,rs*bd[flr][i])


for t in range(1,int(input())+1):
    n=int(input())
    bd = []
    for i in range(n):
        bd.append([i/100 for i in list(map(int, input().split()))])
    mx = 0
    setting()
    print('#{}'.format(t), '{:.6f}'.format(mx*100))

