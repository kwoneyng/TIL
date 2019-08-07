for T in range(int(input())):
    N = input()
    case = []
    for i in N:
        case.append(int(i))
    care = 0
    buy = 0
    for j in case:
        care += j
        if care > 0 :
            care -= 1
        else :
            buy += 1
    print('#{}'.format(T+1),end=' ')
    print(buy)
    