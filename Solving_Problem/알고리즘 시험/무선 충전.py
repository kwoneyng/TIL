from pprint import pprint

for T in range(int(input())):
    m, a = list(map(int, input().split()))
    walk_A = list(map(int, input().split()))
    walk_B = list(map(int, input().split()))
    volt = 0
    ready = []
    A_lo = [0,0]
    B_lo = [9, 9]
    near = [(-1,0), (0,1), (1,0), (0,-1)]
    q = []
    charging = [[] for i in range(a)]
    ap_set = []
    for i in range(a):
        vis = [[0]*20 for i in range(20)]
        y, x, d, ap = list(map(int, input().split()))
        y -= 1
        x -= 1
        ap_set.append(ap)
        q.append([x, y, d])
        while q:
            x, y, d = q.pop(0)
            charging[i].append([x, y])
            vis[x][y] = 1
            for dy, dx in near:
                xi = x+dx
                yi = y+dy
                if 0 <= xi < m and 0 <= yi < m:
                    if vis[xi][yi] == 0:
                        vis[xi][yi] = 1
                        if d > 0 :
                            q.append([xi, yi, d-1])
    for time in range(m+1):
        stay_ap = [[] for i in range(2)]
        # 충전 되니?
        for i in range(a):
            if A_lo in charging[i]:
                stay_ap[0].append(i)
            if B_lo in charging[i]:
                stay_ap[1].append(i)
        for i in range(2):
            if len(stay_ap[i]) == 0:
                stay_ap[i].append(100)
        
        # 뭘로 충전할래?
        su = []
        for i in stay_ap[0]:
            for j in stay_ap[1]:
                su.append([i, j])
        mx = 0
        for i in su:
            cha = 0
            for j in range(a):
                if j in i:
                    cha += ap_set[j]
                    if cha > mx :
                        mx = cha
        volt += mx
        if time == m :
            break
        # 움직이자
        step_a = walk_A
        step_b = walk_B
        if step_a[time] == 1:
            A_lo[0] -= 1
        elif step_a[time] == 2:
            A_lo[1] += 1
        elif step_a[time] == 3:
            A_lo[0] += 1
        elif step_a[time] == 4:
            A_lo[1] -= 1
        if step_b[time] == 1:
            B_lo[0] -= 1
        elif step_b[time] == 2:
            B_lo[1] += 1
        elif step_b[time] == 3:
            B_lo[0] += 1
        elif step_b[time] == 4:
            B_lo[1] -= 1
    print('#{}'.format(T+1),volt)