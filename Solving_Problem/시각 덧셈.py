test_num = int(input())
for i in range(test_num):
    r_h = 0
    r_m = 0
    h1, m1, h2, m2 = list(map(int,input().split()))
    r_h = h1 + h2
    r_m = m1 + m2
    if r_m >= 60:
        r_m = r_m - 60
        r_h = r_h + 1
    if r_h > 12 :
        r_h = r_h - 12
    print(f'#{i+1} {r_h} {r_m}')
