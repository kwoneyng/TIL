def lssl(str, first, last, reverse=False):
    rs = ''
    if reverse == False:
        for i in range(first,last):
            rs += str[i]
    else:
        for i in range(last-1,first-1,-1):
            rs += str[i]
    return rs


def find(st):
    pal_set = []
    for k in st:
        for t_var in range(2, len(st)+1):
            for i in range(len(st)-t_var+1):
                cnt = 0
                for j in range(t_var//2):
                    a = k[i+j]
                    b = k[i+t_var-j-1]
                    if a == b:
                        cnt += 1
                    else:
                        break
                if cnt == t_var//2:
                    pal_set.append(k[i:i+t_var])
    rs = ''
    for i in pal_set:
        if len(i) == n:
            rs = i
    return rs

def rotation(ls):
    bd = []
    for x in range(len(ls)):
        su = []
        for y in range(len(ls)):
            su.append(0)
        bd.append(su)
    for x in range(len(ls)):
        for y in range(len(ls)):
            bd[x][y] = ls[y][x]
    rs = []
    for i in bd:
        rs.append(''.join(i))
    
    return rs




for T in range(int(input())):
    f, n = list(map(int, input().split()))
    st_set = []
    for case in range(f):
        st_set.append(input())
    rs =[]
    rs += [find(st_set)]
    rs += [find(rotation(st_set))]
    print(f'#{T+1} ',end='')
    for i in rs:
        if len(i) > 1:
            print(i)
    