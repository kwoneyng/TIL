test_num = int(input())
for i in range(test_num):
    test_case = int(input())
    str_num = str(test_case)
    key_set = set()
    num_set = set()
    N = 0
    while len(key_set) < 10 :
        N += 1
        str_num = str(test_case * N)
        num_set = set(str_num)
        key_set.update(num_set)
    print(f'#{i+1} {N*test_case}')
