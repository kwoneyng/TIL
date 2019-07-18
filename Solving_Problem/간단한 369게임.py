test_num = int(input())
su = []
str_su =[]
counts = []
minus = []
mk_min = ''
result = ''
for i in range(1,test_num+1):
    su.append(i) 
str_su = list(map(str,su))
for i in range(len(str_su)) :
    count = 0
    for j in str_su[i] :
        if j == '3' or j == '6' or j == '9' :
            count +=1
    counts.append(count)

for i in counts :
    if i >0 :
        for j in range(i) :
            mk_min = mk_min + "-"
        minus.append(mk_min)    
        mk_min = ''
    else : 
        minus.append(i)
result = str_su[0]
for i in range(1, test_num) :
    if counts[i] == 0 :
        result = result + ' ' + str_su[i]
    else :
        result = result + ' ' + minus[i]

print(result)
