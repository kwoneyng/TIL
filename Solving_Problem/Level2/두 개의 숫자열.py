for i in range(int(input())):
    N, M = list(map(int, input().split()))  # 변수설정~
    A_i = list(map(int, input().split()))
    B_j = list(map(int, input().split()))
    max = 0
    if len(A_i) > len(B_j):  # 둘중에 누가 더 긴지 찾아봅시다
        for j in range(len(A_i) - len(B_j) + 1):  # 계산을 하면서 최대값을 찾습니다.
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
