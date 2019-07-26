test_num = int(input())
for i in range(test_num):  # 변수설정
    test_case = int(input())
    str_num = str(test_case)  # 숫자를 하나씩 쪼개줍니다.
    key_set = set()
    num_set = set()
    N = 0
    while len(key_set) < 10 :  # key_set 이 0~9까지 모으는 셋입니다.
        N += 1
        str_num = str(test_case * N)  # N을 곱해가며 곱한수를 쪼개줍니다.
        num_set = set(str_num)  # 쪼갠 숫자를 하나씩 집어넣습니다.
        key_set.update(num_set)  # 나온 숫자 셋을 큰 틀에 넣습니다.
    print(f'#{i+1} {N*test_case}')
