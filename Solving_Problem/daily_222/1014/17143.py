r,c,m = map(int,input().split())
bd = [[[] for i in range(101)] for i in range(101)]
q = []
rs = 0
for i in range(m):
    tr,tc,s,d,z = map(int,input().split())
    if d <= 2:
        s %= (r*2-2)
    else:
        s %= (c*2-2)
    if not bd[tr][tc]:
        bd[tr][tc].append([s,d,z])
        q.append([tr,tc])
    else:
        if z > bd[tr][tc][2]:
            bd[tr][tc][0] = [s,d,z]
for man in range(1,c+1):
    for i in range(1,r+1):
        if bd[i][man]:
            s,d,z = bd[i][man].pop()
            q.pop(q.index([i, man]))
            rs += z
            break
    eat = []
    for k in range(len(q)-1,-1,-1):
        tr,tc = q.pop(k)
        if not bd[tr][tc]:
            continue
        else:
            s,d,z = bd[tr][tc].pop(0)
        for i in range(s):
            if d == 1:
                tr -= 1
            elif d == 2:
                tr += 1
            elif d == 3:
                tc += 1
            elif d ==4 :
                tc -= 1
            if tr == 0:
                d = 2
                tr += 2
            elif tr == r+1:
                d = 1
                tr -= 2
            elif tc == 0:
                d = 3
                tc += 2
            elif tc == c+1:
                d = 4
                tc -= 2
        if bd[tr][tc]:
            eat.append([tr,tc])
        bd[tr][tc].append([s,d,z])
        q.append([tr, tc])
    for tr, tc in eat:
        if len(bd[tr][tc]) > 1:
            bd[tr][tc].sort(key=lambda x:x[2],reverse=True)
            del bd[tr][tc][1:]
print(rs)

