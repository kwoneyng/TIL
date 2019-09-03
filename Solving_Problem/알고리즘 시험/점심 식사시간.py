for T in range(int(input())):
    n = int(input())
    bd = []
    people_o = []
    ext = []
    mn_mn = 1000
    stair1 = [] # 0  bd[ext[0][0]][ext[0][1]]
    stair2 = [] # 1  bd[ext[1][0]][ext[1][1]]
    p_stair1 = []
    p_stair2 = []
    people = []
    result = []

    for i in range(n):
        bd.append(list(map(int, input().split())))
    for x in range(n):
        for y in range(n):
            if bd[x][y] == 1:
                people_o.append([x, y])
            elif bd[x][y] > 1:
                ext.append([x, y])
                
    d_st1 = bd[ext[0][0]][ext[0][1]]
    d_st2 = bd[ext[1][0]][ext[1][1]]               
    
    rs_set = []
    for i in range(1<<len(people_o)):
        su = []
        for j in range(len(people_o)):
            if i&(1<<j):
                su.append(1)
            else:
                su.append(0)
        rs_set.append(su)    

    sa = [0]
    people = [i[:] for i in people_o]
    for i in range(len(people)):
        x, y = people.pop(0)
        e_x, e_y = ext[sa[i]]
        dist = abs(x-e_x)+abs(y-e_y)
        people.append([sa[i], dist])

# 사람과 출구 연결 모든 경우 만들기
    minute = 0
    while True:
        minute += 1
        if mn_mn <= minute :
            break
        gone = []
        while True:
            if len(stair1) < 3:
                if p_stair1:
                    stair1.append(p_stair1.pop(0))
                else:
                    break
            else:
                break
        while True:    
            if len(stair2) < 3:
                if p_stair2:
                    stair2.append(p_stair2.pop(0))
                else: 
                    break
            else:
                break

        for i in range(len(people)):
            people[i][1] -= 1
            if people[i][1] == 0:
                if people[i][0] == 0:
                    p_stair1.append(d_st1)
                    gone.append(i)
                if people[i][0] == 1:
                    p_stair2.append(d_st2)
                    gone.append(i)
        gone.sort(reverse=True)
        for i in gone:
            people.pop(i)
        cn = 1
        while True:
            rs = 0
            for i in range(len(stair1)): # pop이 되어서 인덱스 오류 발생
                stair1[i] -= cn
                if stair1[i] == 0:
                    stair1.pop(i)
                    rs = 1
                    break

            for i in range(len(stair2)):
                stair2[i] -= cn
                if stair2[i] == 0:
                    stair2.pop(i)
                    rs = 1
                    break
            cn = 0
            if rs == 0:
                break

        if not people and not stair1 and not stair2 and not p_stair1 and not p_stair2:
            if minute < mn_mn:
                mn_mn = minute
                result.append(minute)
            break
    print('#{}'.format(T+1),min(result))
