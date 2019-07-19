test_num = int(input())
for i in range(test_num):
    test_case = int(input())
    a, b, c, d, e= (0, 0, 0, 0, 0)

    while test_case > 2 :
        if test_case % 2 == 0 :
            a += 1
            test_case = round(test_case / 2)
        elif test_case % 3 == 0 :
            b += 1
            test_case = round(test_case / 3)
        elif test_case % 5 == 0:
            c += 1
            test_case = round(test_case / 5)
        elif test_case % 7 == 0 :
            d += 1
            test_case = round(test_case / 7)
        elif test_case % 11 == 0 :
            e += 1
            test_case = round(test_case / 11)
        else : 
            print("이상")
            test_case = 0
    print(f'#{i+1} {a} {b} {c} {d} {e}')
