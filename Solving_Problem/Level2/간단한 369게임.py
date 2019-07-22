test_num = int(input())  #변수설정~
su = []
str_su =[]
counts = []
minus = []
mk_min = ''
result = ''
for i in range(1,test_num+1):  # 1~설정한 수까지 list를 만들어줌
    su.append(i) 
str_su = list(map(str,su))  # 우리는 3이 있을때마다 -표시를 섞어서 해야하므로 위의 수를 모두 str으로 변환시켜준다
for i in range(len(str_su)) :  # 3, 6, 9를 찾아봅시다.
    count = 0  # 얘는 왜 여기있을까요?
    for j in str_su[i] :
        if j == '3' or j == '6' or j == '9' :
            count +=1
    counts.append(count)

for i in counts :  # -를 넣는 과정입니다.
    if i >0 :
        for j in range(i) :
            mk_min = mk_min + "-"
        minus.append(mk_min)    
        mk_min = ''
    else : 
        minus.append(i)
result = str_su[0]
for i in range(1, test_num) :  # 섞어주는 과정입니다.
    if counts[i] == 0 :
        result = result + ' ' + str_su[i]
    else :
        result = result + ' ' + minus[i]

print(result)
