test_num = int(input())
test_case = []
month = []
count = []
for i in range(0, test_num)	:
    test_case.append(input())
    month.append(test_case[i][4:6])
print(test_case)
print(month)
for j in range(0, test_num) :
    if month[i] == '01' :
        count.append('31')
    elif month[i] == '02' :
        count.append('28')
    else count.append('30')
print(count)