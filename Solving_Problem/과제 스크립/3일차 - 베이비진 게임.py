for t in range(int(input())):
    flag = 0
    card = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    for i in range(6):
        if flag != 0:
            break
        p1[card[i*2]] += 1
        if i >= 3:
            for j in p1:
                if j == 3:
                    flag = 1
                    break
            if flag == 0:
                for j in range(8):
                    if p1[j] > 0 and p1[j+1] > 0 and p1[j+2] > 0:
                        flag = 1
                        break

        p2[card[i*2+1]] += 1
        if i >= 3:    
            if flag == 0:
                for j in p2:
                    if j == 3:
                        flag = 2
                        break
            if flag == 0:
                for j in range(8):
                    if p2[j] > 0 and p2[j+1] > 0 and p2[j+2] > 0:
                        flag = 2
                        break
    print('#{}'.format(t+1),flag)