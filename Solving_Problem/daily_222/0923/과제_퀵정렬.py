def q_sort(ls,st,ed):
    if st >= ed:
        return
    p=(st+ed)//2
    pv=ls[p]
    i=st
    j=ed
    flag = 0
    while i <= j:
        while ls[i] < pv:
            i += 1
        while pv < ls[j]:
            j -= 1
        if i <= j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
    q_sort(ls,st,i-1)
    q_sort(ls,i,ed)


for t in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))
    q_sort(ls,0,n-1)
    print('#{}'.format(t+1),ls[n//2])