def find(st,ed,i,nx=0):
    global rs
    if st > ed :
        return 0
    m = (st+ed)//2
    if i < als[m]:
        ed = m-1
        if nx == 0 or nx == 2:
            nx = 1
            find(st,ed,i,nx)
    elif i > als[m]:
        st = m+1
        if nx == 0 or nx == 1:
            nx = 2
            find(st,ed,i,nx)
    elif i == als[m]:
        rs += 1
        return 0


for t in range(int(input())):
    n,m = map(int,input().split())
    als=[i for i in list(map(int,input().split()))]
    bls=[i for i in list(map(int,input().split()))]
    als.sort()
    rs = 0
    for i in bls:
        find(0,len(als)-1,i)
    print('#{}'.format(t+1),rs)