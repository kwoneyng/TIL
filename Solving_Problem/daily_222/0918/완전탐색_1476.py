e,s,m = map(int, input().split())  # 0 < e < 16, 0 < s < 29, 0 < m < 20
cnt = 0
my_e = my_s = my_m = 0
while True:
    cnt += 1
    my_e += 1
    my_m += 1
    my_s += 1
    if my_e > 15:
        my_e = 1
    if my_s > 28:
        my_s = 1
    if my_m > 19:
        my_m = 1
    if [my_e, my_s, my_m] == [e,s,m]:
        print(cnt)
        break