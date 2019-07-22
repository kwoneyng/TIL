start = int(input())
for m in range(10) :  # 변수 설정
    test_dep = int(input())
    print(f'#{test_dep}')
    floor = []
    for i in range(test_dep) :  # 한층씩 쌓아주고있습니다.
        obj = []
        for j in range(i+1) :
            if i < 2 :
                obj.append(1)
            else :
                if j == 0 or j == i :
                    obj.append(1)
                else :
                    obj.append(floor[i-1][j-1]+floor[i-1][j])
        floor.append(obj)
    for i in range(test_dep):  # 대입해주고 있습니다.
        result = str(floor[i][0])
        for j in range(1, i+1):
            result = result + ' ' + str(floor[i][j])
        print(result)    
        