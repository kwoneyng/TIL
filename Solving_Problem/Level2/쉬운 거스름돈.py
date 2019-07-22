test_num = int(input())

for i in range(test_num):
    test_case = int(input())  # 횟수 및 변수 초기화
    om = 0
    im = 0
    oc = 0
    ic = 0
    ob = 0
    ib = 0
    ot = 0
    ten = 0
    while test_case >= 10 :  # 큰수부터 차례대로 쪼개는 과정입니다
        if test_case // 50000 > 0 :
            om = test_case // 50000
            test_case = test_case % 50000
        elif test_case // 10000 > 0 :
            im = test_case // 10000
            test_case = test_case % 10000
        elif test_case // 5000 > 0 :
            oc = test_case // 5000
            test_case = test_case % 5000
        elif test_case // 1000 > 0 :
            ic = test_case // 1000
            test_case = test_case % 1000
        elif test_case // 500 > 0 :
            ob = test_case // 500
            test_case = test_case % 500
        elif test_case // 100 > 0 :
            ib = test_case // 100
            test_case = test_case % 100
        elif test_case // 50 > 0 :
            ot = test_case // 50
            test_case = test_case % 50
        else :
            ten = test_case // 10
            test_case = test_case % 10
    print(f'''#{i+1}\n{om} {im} {oc} {ic} {ob} {ib} {ot} {ten}''')
            
