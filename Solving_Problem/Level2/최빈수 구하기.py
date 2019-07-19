import operator

for i in range(int(input())):
    test_no = int(input())
    li_Stu = list(map(int, input().split()))
    a = {}
    for j in range(1, 101):
        a[j] = li_Stu.count(j)  #dict 변환
    c = sorted(a.items(), key=operator.itemgetter(1))
    b = sorted(a.items(), key = operator.itemgetter(0))
    print(f'#{i+1} {c[-1][0]}')  #itemgetter index가 2번째를 기준으로 max값을 찾음
    