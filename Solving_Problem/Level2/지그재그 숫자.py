test_num = int(input())
for i in range(test_num):
    result = 0
    test_case = int(input())
    for j in range(1,test_case + 1):
        if j%2 == 1 :
            result = result + j
        else :
            result = result - j
    print(f'#{j} {result}')
