for i in range(int(input())):
    N, M = list(map(int, input().split()))
    A_i = list(map(int, input().split()))
    B_j = list(map(int, input().split()))
    max = 0
    if len(A_i) > len(B_j):
        for j in range(len(A_i) - len(B_j) + 1):
            sum = 0
            for k in range(len(B_j)):
                sum = sum + A_i[k+j] * B_j[k]
            if max < sum :
                max = sum

    else :
        for j in range(len(B_j) - len(A_i) + 1):
            sum = 0
            for k in range(len(A_i)):
                sum = sum + A_i[k] * B_j[k+j]
            if max < sum :
                max = sum
    print(f'#{i+1} {max}')
