from collections import deque

def sel_ta(ls):
    if len(ls) == 8:
        ls[3:0] = [0]
        # 야구경기 시작
        rs = 0
        out_cnt = 0
        taja = 0
        for i in range(inn):
            ground = deque()
            sco, taja = eachinn(rs,out_cnt,taja,inn)
            rs += sco
        mx = max(rs,mx)
        return 
    for i in range(9):
        if vis[i] == 0:
            vis[i] = 1
            sel_ta(ls+[i])
            vis[i] = 0

def eachinn(rs,ocnt,taja,cur_inn):
    while ocnt < 3:
        do = tasun[taja%9]
        if do == 0:
            onct += 1
            taja += 1
        elif do == 1:
            ground.append(1)
            taja += 1
        elif do == 2:
            ground.append(1)
            ground.append(0)
            taja += 1
        elif do == 3:
            ground.append(1)
            ground.append(0)
            ground.append(0)
            taja += 1
        elif do == 4:
            ground.append(1)
            rs += sum(ground)
            ground = []
            taja += 1

    return rs,taja%9


tasun = []
data = []
vis=[0]*9
vis[0] = 1
mx = 0
inn = int(input())
for i in range(inn):
    data.append(list(map(int,input().split())))
sel_ta(tasun)