test_num = int(input())
for i in range(test_num):
    r_h = 0
    r_m = 0
    h1, m1, h2, m2 = list(map(int,input().split()))  # 받아온 변수를 지정해줍니다.
    r_h = h1 + h2  # 시간 부분입니다.
    r_m = m1 + m2  # 분 부분입니다.
    if r_m >= 60:  # 60분이 넘어가면 1시간을 올려줬습니다.
        r_m = r_m - 60
        r_h = r_h + 1
    if r_h > 12 :  # 12시가 넘어가면 시간을 바꿔서 보여줬습니다. (AM, PM)
        r_h = r_h - 12
    print(f'#{i+1} {r_h} {r_m}')
