test_num = int(input())
test_case = []
month = []
for i in range(0, test_num)	:
    test_case.append(input())
    month.append(test_case[i][4:6])
print(test_case)
print(month)