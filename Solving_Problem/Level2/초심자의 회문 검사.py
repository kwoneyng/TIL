test_num = int(input())
result = []
for i in range(test_num):
    str_set = input()
    re_str_set = str_set[::-1]
    if str_set == re_str_set :
        result.append(1)
    else :
        result.append(0)
for i in range(test_num):
    print(f'#{i+1} {result[i]}')