test_num = int(input())
C_A, C_B = 0, 0
for i in range(test_num):
    Q = list(map(int, input().split()))
    W = Q[4]
    A_r = Q[0]
    B_b = Q[1]
    B_c = Q[2]
    B_r = Q[3]
    result_A = 0
    result_B = 0
    result_A = W*A_r
    if W < B_c :
        result_B = B_b
    else :
        result_B = B_b + (W-B_c)*B_r
    if result_A > result_B:
        print(f'#{i+1} {result_B}')
    else :
        print(f'#{i+1} {result_A}')
