test_num = int(input())
for i in range(test_num):
    test_case, key_size = list(map(int, input().split()))
    loc_X = []
    loc_Y = []
    for j in range(test_case):
        loc_Y=list(map(int, input().split()))
        loc_X.append(loc_Y)
    print(loc_X)