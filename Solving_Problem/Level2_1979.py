test_num = int(input())
for i in range(test_num):
    test_case, key_size = list(map(int, input().split()))
    loc_X = []
    loc_Y = []
    for j in range(test_case):
        loc_Y=list(map(int, input().split()))
        loc_X.append(loc_Y)
    count_X = []
    count_Y = []
    for k in range(test_case):
        sw_X = 1
        N_X = 0
        for z in range(test_case - 1):
            if loc_X[k][z] == 1 and loc_X[k][z+1] == 1 :
                sw_X +=1
            else :
                sw_X = 1
            if sw_X == key_size :
                if z+2 < test_case :
                    if loc_X[k][z+2] != 1 :
                        N_X += 1
                else :
                    N_X += 1
        count_X.append(N_X)
    for b in range(test_case) :
        sw_Y = 1
        N_Y = 0
        for a in range(test_case - 1):
            if loc_X[a][b] == 1 and loc_X[a+1][b] == 1 :
                sw_Y += 1
            else :
                sw_Y = 1
            if sw_Y == key_size :
                if a+2 < test_case :
                    if loc_X[a+2][b] != 1 :
                        N_Y += 1
                else :
                    N_Y += 1
        count_Y.append(N_Y)
    print(f'#{i+1} {sum(count_X)+sum(count_Y)}')