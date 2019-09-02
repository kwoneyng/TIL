def move(ls):
    global n
    xy, b, d = ls
    x, y = xy
    if d == 1:
        x -= 1
        if x == 0:
            b //= 2
            d = 2
    if d == 2 :
        x += 1
        if x == n-1:
            b //= 2
            d = 1
    if d == 3 :
        y -= 1
        if y == 0 :
            b //= 2
            d = 4
    if d == 4 :
        y += 1
        if y == n-1 :
            b //= 2
            d = 3
    rs = [[x,y], b, d]
    if [x, y] not in q:
        q.append([x, y])
        fin_ls.append(rs)
    elif [x, y] not in col :
        col.append([x, y])
        fin_ls.append(rs)


def merge(ls):
    ls1 = []
    for i in fin_ls:
        for j in ls:
            if j not in i:
                s_ls.append(i)
            else :
                ls1.append(i)
    ls1.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(ls1)-1):
        ls1[0][1] += ls1.pop()[1]
    s_ls.append(ls1[0])


for T in range(int(input())):
    n, m, k = list(map(int, input().split()))
    q = []
    s_ls = []
    col = []
    for i in range(k):
        x, y, b, d = list(map(int, input().split()))
        q.append([x, y])
        s_ls.append([[x, y], b, d])
    while m > 0:
        m -= 1
        fin_ls = []
        for i in range(len(q)):
            a = s_ls.pop(0)
            q.pop()
            move(a)
        merge(col)
    print(s_ls)