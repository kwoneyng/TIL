def div(ls, chk, start=1, temp_ls=[]):
    if len(temp_ls) == 2:
        ls.append(temp_ls)
        return 
    for i in range(start, chk):
        div(ls, chk, i+1, temp_ls+[i])


def calc(div_ls, rc):
    global n, m, mx 
    if rc == 0:
        for first, second in div_ls:
            rs_set = []
            rs = 1
            temp = 0    
            for x in range(first):
                for y in range(m):
                    temp += bd[x][y]
            rs_set.append(temp)
            temp = 0
            for x in range(first,second):
                for y in range(m):
                    temp += bd[x][y]
            rs_set.append(temp)
            temp = 0
            for x in range(second,n):
                for y in range(m):
                    temp += bd[x][y]
            rs_set.append(temp)
            for i in rs_set:
                rs *= i
            if mx < rs:
                mx = rs
    else:
        for first, second in div_ls:
            rs_set = []
            rs = 1
            temp = 0    
            for y in range(first):
                for x in range(n):
                    temp += bd[x][y]
            rs_set.append(temp)
            temp = 0
            for y in range(first,second):
                for x in range(n):
                    temp += bd[x][y]
            rs_set.append(temp)
            temp = 0
            for y in range(second,m):
                for x in range(n):
                    temp += bd[x][y]
            rs_set.append(temp)
            for i in rs_set:
                rs *= i
            if mx < rs:
                mx = rs


def l_col(a,b):
    global mx
    rs_set = []
    rs = 1
    temp = 0    
    for y in range(b):
        for x in range(n):
            temp += bd[x][y]
    rs_set.append(temp)
    temp = 0
    for x in range(a):
        for y in range(b,m):
            temp += bd[x][y]
    rs_set.append(temp)
    temp = 0
    for x in range(a,n):
        for y in range(b,m):
            temp += bd[x][y]
    rs_set.append(temp)
    for i in rs_set:
        rs *= i
    if mx < rs:
        mx = rs

def r_col(a,b):
    global mx
    rs_set = []
    rs = 1
    temp = 0    
    for x in range(a):
        for y in range(b):
            temp += bd[x][y]
    rs_set.append(temp)
    temp = 0
    for x in range(a,n):
        for y in range(b):
            temp += bd[x][y]
    rs_set.append(temp)
    temp = 0
    for x in range(n):
        for y in range(b,m):
            temp += bd[x][y]
    rs_set.append(temp)
    for i in rs_set:
        rs *= i
    if mx < rs:
        mx = rs        

n, m = map(int, input().split())
bd = []
for i in range(n):
    a = list(input())
    bd.append(list(map(int,a)))
#가로로 나눌 때와 세로로 나눌 때
row_set=[]
col_set=[]
mx = 0
div(row_set, n)
div(col_set, m)
calc(row_set,0)
calc(col_set,1)
for x in range(1,n):
    for y in range(1,m):
        l_col(x,y)
        r_col(x,y)
print(mx)