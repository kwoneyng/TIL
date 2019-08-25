N = int(input())
su = []
for i in range(1,N+1):
    cnt = 0
    ls = []
    ls.append(N)
    ls.append(i)
    j = 0
    while True:
        nxt = ls[j] - ls[j+1]
        if nxt < 0:
            break
        ls.append(nxt)
        j += 1
    su.append([i, len(ls)])
op = max(su,key=lambda x:x[1])
rs = []
rs.append(N)
rs.append(op[0])
p = 0
while True:
    nxt = rs[p] - rs[p+1]
    if nxt < 0:
        break
    rs.append(nxt)
    p += 1
print(op[1])
rs = map(str, rs)
print(' '.join(rs))

