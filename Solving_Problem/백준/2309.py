t_set = []
for T in range(9):
    t_set.append(int(input()))
t_set.sort()
rs = []
a = 0b1111111
val = []
for i in range(a, 1<<9):
    su = 0
    for j in range(9):
        if i & (1<<j) :
            su += 1
    if su == 7 :
        val.append(format(i,'b'))
for i in range(len(val)) :
    while len(val[i]) < 9 :
        val[i] = '0'+val[i]
for i in range(len(val)):
    tall = 0
    for j in range(len(val[i])):
        if val[i][j] == '1':
            tall += t_set[j]
    if tall == 100:
        rs.append(int(format(i,'d')))
for i in range(len(val[rs[0]])):
    if val[rs[0]][i] == '1':
        print(t_set[i])
        