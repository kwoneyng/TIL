for i in range(int(input())):
    test = input()
    can = []
    for j in range(len(test)):
        if test[0:j] == test[j: j*2]:
            if j >= 1 :
                can.append(j)   # 1~j번 까지 글자 == j+1~2j 까지 글자
    if len(can) > 1:
        for j in range(len(can)-1):
            if can[0] != 1:
                if can[1]%can[0] == 0 :
                    can.pop(1)
            else :
                if can[2]%can[1] == 0 :
                    can.pop(2)
    print(f'#{i+1} {max(can)}')
