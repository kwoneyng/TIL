def cmx(**kwargs):
    mx = 0
    mx_key = []
    for i in kwargs.items():
        if i[1] > mx:
            mx = i[1]
    
    for j in kwargs.items():
        if j[1] == mx :
            mx_key.append(j[0])
    return mx_key, mx

for T in range(int(input())):
    n = int(input())
    su_set = []
    su_dict = {}
    mx = 0
    for i in input():
        su_set.append(i)
    for i in su_set:
        if i not in su_dict:
            su_dict[i] = 1
        else :
            su_dict[i] += 1
    a = cmx(**su_dict)[0]
    su_max = cmx(**su_dict)[1]
    for k in a:
        if int(k) > mx:
            mx = int(k)
    print('#{0} {1} {2}'.format(T+1, mx, su_max))