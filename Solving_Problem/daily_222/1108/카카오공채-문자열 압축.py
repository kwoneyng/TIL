def cut(dan, data):
    global mn
    q = []
    st = ''
    for i in range(len(data)//dan):
        q.append(''.join(data[i*dan:(i+1)*dan]))
    rem = ''.join(data[(i+1)*dan:])
    if rem:
        q.append(rem)

    rs = 1
    rst = ''
    for i in range(len(q)):
        rss = q[i]
        if i+1 < len(q) and q[i] == q[i+1]:
            rs += 1
        elif rs > 1:
            rst = rst + str(rs) + rss 
            rs = 1
        else :
            rst = rst + rss
    mn = min(mn,len(rst))

data = list(input())
mn = 10000
for i in range(1,len(data)//2+1):
    cut(i,data)
print(mn)