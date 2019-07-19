test_num = int(input())
kill = []
max_kill = []
for i in range(test_num) :
    Ip_data = list(map(int,input().split()))
    test_case = Ip_data[0]
    size = Ip_data[1]
    plate_X=[]
    for j in range(test_case) : 
        plate_Y = list(map(int,input().split()))
        plate_X.append(plate_Y)
    if(test_case > size) :
        kill=[]
        for j in range(test_case - size + 1) :
            for k in range(test_case - size + 1) :
                kill_sum = []
                for zx in range(size) :
                    for zy in range(size) :
                        kill_sum.append(plate_X[j+zx][k+zy])
                kill.append(sum(kill_sum))
        max_kill.append(max(kill))

for num in range(test_num) :
    print(f'#{num+1} {max_kill[num]}')
