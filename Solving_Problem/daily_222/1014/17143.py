R,C,M = map(int, input().split())
bd = [[-1]*101 for i in range(101)] 
r = []
c = []
s = []
d = []
z = []
for i in range(M):
    tr,tc,ts,td,tz = map(int,input().split())
    bd[tr][tc] = i
    r.append(tr)
    c.append(tc)
    s.append(ts)
    d.append(td)
    z.append(tz)
rs = 0
for man in range(C):
    catch = 0
    mn = 999
    eat = []
    for i in range(len(r)):
        if c[i] == man:
            if r[i] < mn:
                mn = r[i]
                catch = i
    bd[r[catch]][c[catch]] = -1
    r.pop(catch)
    c.pop(catch)
    s.pop(catch)
    d.pop(catch)
    rs += z.pop(catch)
    for i in range(len(r)):
        if d[i] = 1:
            dis = -1
            for 
print(rs)
