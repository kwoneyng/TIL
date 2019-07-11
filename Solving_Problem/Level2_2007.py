test_num = int(input())
for i in range(test_num):
    k = 1
    test_case = input()   # test_case[] 가 30마디
    while test_case[0:k] != test_case[k:k*2] :
        k += 1
    print(f'#{i+1} {k}')
