test_num = int(input())
for i in range(test_num):
    result = 0
    num_list = list(map(int, input().split()))
    
    result = sum(num_list)-max(num_list)-min(num_list)
    print(f'#{i+1} {round(result/(len(num_list)-2))}')