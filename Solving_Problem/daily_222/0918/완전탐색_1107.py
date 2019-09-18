def perm(ln, ls=[]):
    if len(ls) == ln:
        if ln == 0:
            return 0
        else :
            temp.append(int(''.join(map(str, ls))))
            return 0
    for i in button:
        perm(ln, ls+[i])

n_st = input()
n = int(n_st)
su = int(input())
dis = list(map(int, input().split()))
button = [i for i in range(0,10)]
rs1 = 100000000
rs2 = 100000000
now = 100
mn = 9999999999999999
temp = []
key = 0
flag = 0
for i in dis:
    button.remove(i)
rs1 = abs(n-100)
if button:
    if n > 9:
        for i in range(-1,2):
            perm(len(n_st)+i)
    for i in temp:
        if abs(i-n) < mn:
            mn = abs(i-n)
            key = len(str(i))
    rs2 = mn + key

if rs1 > rs2:
    print(rs2)
else: 
    print(rs1)
