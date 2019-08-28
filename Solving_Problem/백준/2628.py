x, y = list(map(int, input().split()))
row = ['0' for i in range(x)]
col = ['0' for i in range(y)]
t_no = int(input())
cut = []
for i in range(t_no):
    cut.append(list(map(int, input().split())))
for i in cut:
    if i[0] == 0:
        col[i[1]] = 'XO'
    else :
        row[i[1]] = 'XO'
a = list(''.join(col).split('X'))
b = list(''.join(row).split('X'))
c = len(max(a,key=lambda x:len(x)))
d = len(max(b,key=lambda x:len(x)))
print(c*d)