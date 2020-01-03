def check(a,b,day=1):
    global rs
    if rs != -1:
        return
        
    if day == ldst:
        rs = ldst-1
        return

    stdd = 1<<(day-1)
    if dst & 1<<day:
        check(a+stdd, b-stdd, day+1)
    else:
        if a-stdd > 0:
            check(a-stdd,b-stdd,day+1)
        if b+stdd <= n:
            check(a+stdd,b+stdd,day+1)
            

def lenchk(dst):
    for i in range(20):
        if 2**(i) <= dst < 2**(i+1):
            return i+1


n,a,b = map(int,input().split())
rs = -1
dst = abs(a-b)
if a > b:
    a,b = b,a

if dst % 2 == 1:
    print(-1)
else:
    ldst = lenchk(dst)
    check(a,b)
    print(rs)